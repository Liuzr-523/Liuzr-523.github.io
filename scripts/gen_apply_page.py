#!/usr/bin/env python3
"""
gen_apply_page.py — 生成 /apply/ 申请账号页面（内嵌 RSA 公钥）

用法:
    python3 scripts/gen_apply_page.py

说明:
    公钥来自 scripts/keys/public_key.pem（本地生成，可公开）
    申请者用公钥加密申请信息，只有私钥能解密（scripts/audit_apply.py）
    生成后覆盖根目录的 apply.md，推送即生效
"""
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PUB_KEY = os.path.join(ROOT, "scripts/keys/public_key.pem")

# 申请者生成密文后，需要发给你的联系方式（写在这里，会显示在页面上）
CONTACT_TEXT = "刘子睿（微信 / 邮箱：待填写）"

if not os.path.exists(PUB_KEY):
    raise SystemExit("❌ 缺少 scripts/keys/public_key.pem，请先生成 RSA 密钥对")

pem = open(PUB_KEY, encoding="utf-8").read().strip()

page = f"""---
layout: page
title: 申请私密账号
permalink: /apply/
---

<div class="container" style="max-width: 520px">
  <h2 class="mb-1">申请私密空间账号</h2>
  <p class="text-muted mb-4">填写信息提交申请，<strong>审核通过后</strong>账号方可使用。</p>

  <form id="applyForm" onsubmit="return false">
    <div class="mb-3">
      <label class="form-label">账号（3-20 位字母 / 数字 / 下划线）</label>
      <input id="f-user" class="form-control" autocomplete="off" />
    </div>
    <div class="mb-3">
      <label class="form-label">密码（至少 8 位）</label>
      <input type="password" id="f-pass" class="form-control" autocomplete="new-password" />
    </div>
    <div class="mb-3">
      <label class="form-label">确认密码</label>
      <input type="password" id="f-pass2" class="form-control" autocomplete="new-password" />
    </div>
    <div class="mb-3">
      <label class="form-label">姓名</label>
      <input id="f-name" class="form-control" autocomplete="off" />
    </div>
    <div class="mb-3">
      <label class="form-label">联系方式（微信 / 邮箱）</label>
      <input id="f-phone" class="form-control" autocomplete="off" />
    </div>
    <button id="f-submit" class="btn btn-primary">生成申请</button>
  </form>

  <div id="f-msg" class="text-danger mt-3"></div>

  <div id="f-result" class="d-none mt-4">
    <div class="alert alert-success">申请已加密生成，别人无法查看。请复制下方密文发给 {CONTACT_TEXT} 审核：</div>
    <textarea id="f-cipher" class="form-control" rows="4" readonly></textarea>
    <button id="f-copy" class="btn btn-outline-primary mt-2">复制密文</button>
    <p class="text-muted small mt-3">审核通过后，用你的账号和密码访问
      <a href="/private/">私密空间</a>。</p>
  </div>
</div>

<script>
  (function () {{
    var PUBLIC_KEY_PEM = {repr(pem)};

    var userEl = document.getElementById("f-user");
    var passEl = document.getElementById("f-pass");
    var pass2El = document.getElementById("f-pass2");
    var nameEl = document.getElementById("f-name");
    var phoneEl = document.getElementById("f-phone");
    var submitBtn = document.getElementById("f-submit");
    var msgEl = document.getElementById("f-msg");
    var resultEl = document.getElementById("f-result");
    var cipherEl = document.getElementById("f-cipher");
    var copyBtn = document.getElementById("f-copy");

    function showMsg(t) {{
      msgEl.textContent = t || "";
    }}

    function pemToArrayBuffer(pem) {{
      var b64 = pem.replace(/-----[^-]+-----/g, "").replace(/\\s+/g, "");
      var bin = atob(b64);
      var bytes = new Uint8Array(bin.length);
      for (var i = 0; i < bin.length; i++) bytes[i] = bin.charCodeAt(i);
      return bytes.buffer;
    }}

    function b64(bytes) {{
      var s = "";
      var arr = new Uint8Array(bytes);
      for (var i = 0; i < arr.length; i++) s += String.fromCharCode(arr[i]);
      return btoa(s);
    }}

    async function encryptPayload(obj) {{
      var key = await crypto.subtle.importKey(
        "spki",
        pemToArrayBuffer(PUBLIC_KEY_PEM),
        {{ name: "RSA-OAEP", hash: "SHA-256" }},
        false,
        ["encrypt"]
      );
      var data = new TextEncoder().encode(JSON.stringify(obj));
      var ct = await crypto.subtle.encrypt({{ name: "RSA-OAEP" }}, key, data);
      return b64(ct);
    }}

    submitBtn.addEventListener("click", async function () {{
      var user = userEl.value.trim();
      var pass = passEl.value;
      var pass2 = pass2El.value;
      var name = nameEl.value.trim();
      var contact = phoneEl.value.trim();

      if (!/^[A-Za-z0-9_]{{3,20}}$/.test(user)) return showMsg("账号需为 3-20 位字母、数字或下划线");
      if (pass.length < 8) return showMsg("密码至少 8 位");
      if (pass !== pass2) return showMsg("两次输入的密码不一致");
      if (!name) return showMsg("请填写姓名");

      showMsg("");
      submitBtn.disabled = true;
      submitBtn.textContent = "生成中…";
      try {{
        var payload = {{
          user: user,
          pass: pass,
          name: name,
          phone: contact,
          ts: new Date().toISOString(),
        }};
        var cipher = await encryptPayload(payload);
        cipherEl.value = cipher;
        resultEl.classList.remove("d-none");
        submitBtn.textContent = "已生成";
      }} catch (e) {{
        showMsg("生成失败：" + e.message);
        submitBtn.disabled = false;
        submitBtn.textContent = "生成申请";
      }}
    }});

    copyBtn.addEventListener("click", function () {{
      cipherEl.select();
      document.execCommand("copy");
      copyBtn.textContent = "已复制 ✓";
      setTimeout(function () {{ copyBtn.textContent = "复制密文"; }}, 1500);
    }});
  }})();
</script>
"""

out = os.path.join(ROOT, "apply.md")
open(out, "w", encoding="utf-8").write(page)
print(f"✅ 已生成 {out}")
print(f"   联系方式文案: {CONTACT_TEXT or '（空，建议在脚本里填上）'}")
