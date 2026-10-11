let currentCid = CURRENT_CID;
let userLang = USER_LANG || "tanglish";

const messagesEl = document.getElementById("messages");
const form = document.getElementById("chatForm");
const input = document.getElementById("userInput");
const langSelect = document.getElementById("langSelect");
const sidebar = document.getElementById("sidebar");
const menuBtn = document.getElementById("menuBtn");

// Language switch
langSelect.addEventListener("change", async () => {
  userLang = langSelect.value;
  await fetch("/api/set_lang", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ lang: userLang }),
  });
});

// Sidebar toggle (mobile)
if (menuBtn) menuBtn.addEventListener("click", () => sidebar.classList.toggle("open"));

// Send message
form.addEventListener("submit", async (e) => {
  e.preventDefault();
  const text = input.value.trim();
  if (!text) return;

  const welcome = messagesEl.querySelector(".welcome");
  if (welcome) welcome.remove();

  appendMessage("user", text);
  input.value = "";

  const typing = appendMessage("bot", "", true);

  try {
    const res = await fetch("/api/send", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        message: text,
        conversation_id: currentCid,
        lang: userLang,
      }),
    });
    const data = await res.json();

    typing.classList.remove("typing");
    typing.querySelector(".bubble").textContent = data.reply || "No response.";

    if (!currentCid && data.conversation_id) {
      currentCid = data.conversation_id;
      history.replaceState(null, "", `/chat?cid=${currentCid}`);
      setTimeout(() => window.location.reload(), 300);
    }
  } catch (err) {
    typing.classList.remove("typing");
    typing.querySelector(".bubble").textContent = "⚠️ Server error. Try again.";
  }
});

function appendMessage(sender, text, typing = false) {
  const div = document.createElement("div");
  div.className = `msg ${sender}${typing ? " typing" : ""}`;
  div.innerHTML = `<div class="bubble"></div>`;
  div.querySelector(".bubble").textContent = text;
  messagesEl.appendChild(div);
  messagesEl.scrollTop = messagesEl.scrollHeight;
  return div;
}

// New chat
document.getElementById("newChatBtn").addEventListener("click", () => {
  window.location.href = "/chat";
});

// Suggestion chips
document.querySelectorAll(".chip").forEach((chip) => {
  chip.addEventListener("click", () => {
    input.value = chip.textContent;
    form.dispatchEvent(new Event("submit"));
  });
});

// Delete chat
document.querySelectorAll(".del-btn").forEach((btn) => {
  btn.addEventListener("click", async (e) => {
    e.stopPropagation();
    if (!confirm("Delete this chat?")) return;
    const cid = btn.dataset.cid;
    await fetch(`/api/delete_chat/${cid}`, { method: "DELETE" });
    btn.closest("li").remove();
    if (parseInt(cid) === currentCid) window.location.href = "/chat";
  });
});

// Load existing chat
document.querySelectorAll("#convList li").forEach((li) => {
  li.addEventListener("click", (e) => {
    if (e.target.classList.contains("del-btn")) return;
    window.location.href = `/chat?cid=${li.dataset.cid}`;
  });
});