const storeKey = "mini-qms-docs";

function loadStore() {
  try {
    return JSON.parse(localStorage.getItem(storeKey) || "{}");
  } catch {
    return {};
  }
}

function saveStore(store) {
  localStorage.setItem(storeKey, JSON.stringify(store));
}

function setBusy(on) {
  document.getElementById("busy").style.display = on ? "block" : "none";
}

function showToast(message) {
  const toast = document.getElementById("toast");
  toast.textContent = message;
  toast.style.display = "block";
  setTimeout(() => {
    toast.style.display = "none";
  }, 800);
}

function render(docId) {
  const store = loadStore();
  const doc = store[docId];
  if (!doc) return;

  document.getElementById("doc-id").textContent = doc.id;
  document.getElementById("doc-title").textContent = doc.title;
  document.getElementById("doc-status").textContent = doc.status;
  document.getElementById("request-review-btn").disabled = doc.status !== "Draft";
  document.getElementById("approve-btn").disabled = doc.status !== "Review requested";

  const tasks = Object.values(store).filter((d) => d.status === "Review requested");
  const taskList = document.getElementById("task-list");
  taskList.innerHTML = "";
  for (const task of tasks) {
    const tr = document.createElement("tr");
    tr.dataset.testid = `task-${task.id}`;
    tr.innerHTML = `<td>${task.id}</td><td>${task.title}</td>`;
    taskList.appendChild(tr);
  }

  const audit = document.getElementById("audit-log");
  audit.innerHTML = "";
  for (const entry of doc.audit || []) {
    const li = document.createElement("li");
    li.textContent = entry;
    audit.appendChild(li);
  }
}

function createDocument() {
  const title = document.getElementById("title-input").value.trim() || "Untitled";
  const id = `doc-${Date.now()}-${Math.floor(Math.random() * 100000)}`;
  const store = loadStore();
  store[id] = {
    id,
    title,
    status: "Draft",
    audit: [`created:${id}`]
  };
  saveStore(store);
  window.location.hash = id;
  render(id);
  showToast("Draft created");
}

function requestReview() {
  const id = window.location.hash.slice(1);
  const store = loadStore();
  const doc = store[id];
  if (!doc || doc.status !== "Draft") return;

  setBusy(true);
  setTimeout(() => {
    doc.status = "Review requested";
    doc.audit.push(`review-requested:${id}`);
    saveStore(store);
    setBusy(false);
    render(id);
    showToast("Review requested");
  }, 250);
}

function approveHeavy() {
  const id = window.location.hash.slice(1);
  const store = loadStore();
  const doc = store[id];
  if (!doc || doc.status !== "Review requested") return;

  setBusy(true);
  // Simulate a slow Edge Function (PDF + upload). Shortened for practice.
  setTimeout(() => {
    doc.status = "Approved";
    doc.audit.push(`approved:${id}`);
    saveStore(store);
    setBusy(false);
    render(id);
    showToast("Approved");
  }, 1200);
}

document.getElementById("create-btn").addEventListener("click", createDocument);
document.getElementById("request-review-btn").addEventListener("click", requestReview);
document.getElementById("approve-btn").addEventListener("click", approveHeavy);

window.addEventListener("hashchange", () => {
  const id = window.location.hash.slice(1);
  if (id) render(id);
});

if (window.location.hash.slice(1)) {
  render(window.location.hash.slice(1));
}
