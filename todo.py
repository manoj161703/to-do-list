import streamlit as st
from datetime import datetime

# -------------------- Page Setup --------------------
st.set_page_config(page_title="Modern To-Do List", page_icon="✅", layout="centered")

st.markdown("""
<style>
:root{
  --bg1:#0f1226; --bg2:#1b2142; --bg3:#0d1222;
  --glass: rgba(255,255,255,0.08);
  --border: rgba(255,255,255,0.14);
  --text:#f2f2f8; --muted:#b7b9c9;
  --accent:#7c5cff; --accent2:#15d1a5; --danger:#ff5577;
}

html, body, [data-testid="stAppViewContainer"]{
  background: radial-gradient(60% 60% at 20% 10%, #13183a, transparent),
              linear-gradient(135deg, var(--bg1), var(--bg2) 45%, var(--bg3));
  color: var(--text);
}
[data-testid="stHeader"]{background:transparent;}

.header{
  margin:18px auto 12px;
  padding:14px 18px;
  border-radius:18px;
  background:linear-gradient(120deg, var(--accent), var(--accent2));
  color:#fff;
  font-weight:800;
  letter-spacing:.4px;
  text-align:center;
  box-shadow:0 16px 40px rgba(124,92,255,.35);
  max-width:520px;
}

.card{
  max-width:520px;
  margin:0 auto 24px;
  background:var(--glass);
  border:1px solid var(--border);
  border-radius:20px;
  padding:22px;
  box-shadow:0 18px 40px rgba(0,0,0,.35);
  backdrop-filter:blur(10px);
}

.task{
  display:flex;
  justify-content:space-between;
  align-items:center;
  padding:6px 10px;
  margin-top:6px;
  border-radius:12px;
  transition:background .15s ease;
}
.task:hover{ background:rgba(255,255,255,0.05); }

.btn-add{
  background:linear-gradient(120deg,var(--accent),var(--accent2));
  color:#fff; border:none;
  border-radius:999px;
  padding:8px 16px;
  font-weight:600;
  cursor:pointer;
}
.btn-add:hover{filter:brightness(1.15);}
.small{font-size:12px;color:var(--muted);}
.done{
  text-decoration:line-through;
  color:var(--muted);
}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="header">🧭 Modern To-Do List</div>', unsafe_allow_html=True)
st.markdown('<div class="card">', unsafe_allow_html=True)

# -------------------- State Init --------------------
if "tasks" not in st.session_state:
    st.session_state.tasks = []
if "completed" not in st.session_state:
    st.session_state.completed = []

# -------------------- Add Task --------------------
st.markdown("### Add a New Task")
col1, col2 = st.columns([4,1])
with col1:
    new_task = st.text_input("Task name", placeholder="Type your task here…", label_visibility="collapsed")
with col2:
    if st.button("➕ Add", use_container_width=True):
        if new_task.strip():
            st.session_state.tasks.append({"task": new_task.strip(), "time": datetime.now().strftime("%H:%M:%S")})
            st.experimental_rerun()

# -------------------- Active Tasks --------------------
if st.session_state.tasks:
    st.markdown("### 🔥 Active Tasks")
    for i, t in enumerate(list(st.session_state.tasks)):
        col1, col2, col3 = st.columns([6,1,1])
        with col1:
            st.markdown(f"<div class='task'>{t['task']} <span class='small'>({t['time']})</span></div>", unsafe_allow_html=True)
        with col2:
            if st.button("✅", key=f"done_{i}"):
                st.session_state.completed.append({"task": t["task"], "time": t["time"]})
                st.session_state.tasks.remove(t)
                st.experimental_rerun()
        with col3:
            if st.button("❌", key=f"del_{i}"):
                st.session_state.tasks.remove(t)
                st.experimental_rerun()
else:
    st.info("No active tasks — you’re all caught up!")

# -------------------- Completed Tasks --------------------
if st.session_state.completed:
    st.markdown("### ✅ Completed")
    for i, t in enumerate(list(st.session_state.completed)):
        col1, col2 = st.columns([7,1])
        with col1:
            st.markdown(f"<div class='task done'>✔️ {t['task']} <span class='small'>({t['time']})</span></div>", unsafe_allow_html=True)
        with col2:
            if st.button("🗑", key=f"clr_{i}"):
                st.session_state.completed.remove(t)
                st.experimental_rerun()

st.markdown("</div>", unsafe_allow_html=True)
