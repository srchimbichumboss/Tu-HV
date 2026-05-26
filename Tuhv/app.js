* ════════════════════════════════════════════════════
   CONSTRUCTOR DE HOJA DE VIDA — app.js
   Lógica completa: formulario, plantillas, PDF, demo
════════════════════════════════════════════════════ */

// ── Estado global ──────────────────────────────────
let state = {
  template: 'dark',
  accent: '#00e5ff',
  name: '',
  job: '',
  about: '',
  photo: null,
  phone: '',
  email: '',
  city: '',
  linkedin: '',
  education: [],
  experience: [],
  skills: [],
  languages: [],
  references: [],
};

let zoom = 90;

// ── Demo data ──────────────────────────────────────
const DEMO = {
  name: 'Thomás Mengual',
  job: 'Técnico Ambiental · Tecnólogo en Gestión de Transporte',
  about: 'Soy técnico en monitoreo ambiental egresado de un colegio militar con énfasis en comercio y sistemas. Me gusta enseñar, aprender e investigar; trabajo en condiciones de alta presión, resuelvo problemas de manera eficiente y cumplo metas en corto tiempo. Poseo buen manejo de las relaciones interpersonales, soy responsable, honesto, dinámico y comprometido con mi trabajo.',
  phone: '321 7046710',
  email: 'mengualarcinegas@gmail.com',
  city: 'Bogotá D.C., Colombia',
  linkedin: 'linkedin.com/in/thomas-mengual',
  education: [
    { year:'2022', title:'Bachiller con especialidad en Comercio y Sistemas', institution:'Colegio Militar Almirante Padilla' },
    { year:'2022', title:'Técnico en Monitoreo Ambiental', institution:'SENA' },
    { year:'2024', title:'Inglés B1', institution:'ILUD Universidad Distrital' },
    { year:'2024', title:'Tecnología en Gestión Integral de Transporte', institution:'SENA' },
    { year:'2025', title:'Curso de Trabajo en Alturas', institution:'MYG' },
  ],
  experience: [
    { company:'MyG Solutions S.A.S', role:'Auxiliar Técnico', period:'2024', description:'Formé parte del equipo encargado de apoyar en la instalación y mantenimiento de los sistemas eléctricos, asegurando la correcta ejecución de las tareas y el cumplimiento de los estándares de calidad y seguridad.' },
    { company:'Aerosán – Área de Exportaciones', role:'Aprendiz / Prácticas SENA', period:'2023', description:'Apoyo en la gestión operativa y documental de procesos de comercio exterior, seguimiento de operaciones internacionales y aplicación de normativa aduanera.' },
  ],
  skills: [
    { name:'Técnico en Monitoreo Ambiental', level:95 },
    { name:'Tecnología en Gestión de Transporte', level:90 },
    { name:'Técnico en Comercio y Sistemas', level:85 },
    { name:'Responsabilidad y liderazgo', level:92 },
    { name:'Trabajo en equipo', level:90 },
    { name:'Aprendizaje continuo', level:88 },
  ],
  languages: [
    { name:'Español', level:'Nativo' },
    { name:'Inglés', level:'Intermedio (B1)' },
  ],
  references: [
    { name:'Luis Fernando Marín Gonzales', role:'Tecnólogo Electricista Independiente', contact:'314-2498739 · Bogotá D.C.' },
    { name:'Maria Fernanda Arcinegas Chavez', role:'Docente', contact:'313-8830976 · Bogotá' },
  ],
};

// ══════════════════════════════════════════════════
//  INIT
// ══════════════════════════════════════════════════
document.addEventListener('DOMContentLoaded', () => {
  setupInputs();
  setupTemplateCards();
  setupColorDots();
  setupPhotoUpload();
  setupDynamicLists();
  setupButtons();
  setupZoom();
  renderCV();
});

// ══════════════════════════════════════════════════
//  INPUTS BÁSICOS
// ══════════════════════════════════════════════════
function setupInputs() {
  const bind = (id, key) => {
    const el = document.getElementById(id);
    if (!el) return;
    el.addEventListener('input', () => { state[key] = el.value; renderCV(); });
  };
  bind('nameInput','name');
  bind('jobInput','job');
  bind('aboutInput','about');
  bind('phoneInput','phone');
  bind('emailInput','email');
  bind('cityInput','city');
  bind('linkedinInput','linkedin');
}

// ══════════════════════════════════════════════════
//  PLANTILLAS
// ══════════════════════════════════════════════════
function setupTemplateCards() {
  document.querySelectorAll('.template-card').forEach(card => {
    card.addEventListener('click', () => {
      document.querySelectorAll('.template-card').forEach(c => c.classList.remove('active'));
      card.classList.add('active');
      state.template = card.dataset.template;
      renderCV();
    });
  });
}

// ══════════════════════════════════════════════════
//  COLORES
// ══════════════════════════════════════════════════
function setupColorDots() {
  document.querySelectorAll('.color-dot').forEach(dot => {
    dot.addEventListener('click', () => {
      document.querySelectorAll('.color-dot').forEach(d => d.classList.remove('active'));
      dot.classList.add('active');
      state.accent = dot.dataset.color;
      renderCV();
    });
  });
}

// ══════════════════════════════════════════════════
//  FOTO
// ══════════════════════════════════════════════════
function setupPhotoUpload() {
  const area = document.getElementById('photoArea');
  const input = document.getElementById('photoInput');
  area.addEventListener('click', () => input.click());
  input.addEventListener('change', e => {
    const file = e.target.files[0];
    if (!file) return;
    const reader = new FileReader();
    reader.onload = ev => {
      state.photo = ev.target.result;
      const thumb = document.getElementById('photoPreviewThumb');
      const placeholder = document.getElementById('photoPlaceholder');
      thumb.src = state.photo;
      thumb.style.display = 'block';
      placeholder.style.display = 'none';
      renderCV();
    };
    reader.readAsDataURL(file);
  });
}

// ══════════════════════════════════════════════════
//  LISTAS DINÁMICAS
// ══════════════════════════════════════════════════
function setupDynamicLists() {
  document.getElementById('addEducationBtn').onclick = () => {
    state.education.push({ year:'', title:'', institution:'' });
    renderEducationList();
    renderCV();
  };
  document.getElementById('addExperienceBtn').onclick = () => {
    state.experience.push({ company:'', role:'', period:'', description:'' });
    renderExperienceList();
    renderCV();
  };
  document.getElementById('addSkillBtn').onclick = () => {
    const name = document.getElementById('skillNewInput').value.trim();
    const level = parseInt(document.getElementById('skillLevel').value);
    if (!name) return;
    state.skills.push({ name, level });
    document.getElementById('skillNewInput').value = '';
    renderSkillsList();
    renderCV();
  };
  document.getElementById('addLangBtn').onclick = () => {
    const name = document.getElementById('langNewInput').value.trim();
    const level = document.getElementById('langLevel').value;
    if (!name) return;
    state.languages.push({ name, level });
    document.getElementById('langNewInput').value = '';
    renderLanguagesList();
    renderCV();
  };
  document.getElementById('addRefBtn').onclick = () => {
    state.references.push({ name:'', role:'', contact:'' });
    renderReferencesList();
    renderCV();
  };
}

function renderEducationList() {
  const container = document.getElementById('educationList');
  container.innerHTML = '';
  state.education.forEach((edu, i) => {
    const div = document.createElement('div');
    div.className = 'dyn-item';
    div.innerHTML = `
      <button class="remove-btn" data-i="${i}" data-type="education"><i class="fas fa-times"></i></button>
      <div class="dyn-label">Año</div>
      <input type="text" placeholder="2024" value="${edu.year}" data-field="year" data-i="${i}" data-type="education"/>
      <div class="dyn-label">Título / Estudio</div>
      <input type="text" placeholder="Tecnología en Gestión..." value="${edu.title}" data-field="title" data-i="${i}" data-type="education"/>
      <div class="dyn-label">Institución</div>
      <input type="text" placeholder="SENA" value="${edu.institution}" data-field="institution" data-i="${i}" data-type="education"/>
    `;
    container.appendChild(div);
  });
  attachDynEvents();
}

function renderExperienceList() {
  const container = document.getElementById('experienceList');
  container.innerHTML = '';
  state.experience.forEach((exp, i) => {
    const div = document.createElement('div');
    div.className = 'dyn-item';
    div.innerHTML = `
      <button class="remove-btn" data-i="${i}" data-type="experience"><i class="fas fa-times"></i></button>
      <div class="dyn-label">Empresa</div>
      <input type="text" placeholder="Empresa S.A.S" value="${exp.company}" data-field="company" data-i="${i}" data-type="experience"/>
      <div class="dyn-label">Cargo</div>
      <input type="text" placeholder="Auxiliar técnico" value="${exp.role}" data-field="role" data-i="${i}" data-type="experience"/>
      <div class="dyn-label">Período</div>
      <input type="text" placeholder="2023 – 2024" value="${exp.period}" data-field="period" data-i="${i}" data-type="experience"/>
      <div class="dyn-label">Descripción</div>
      <textarea placeholder="Describe tus responsabilidades y logros..." data-field="description" data-i="${i}" data-type="experience">${exp.description}</textarea>
    `;
    container.appendChild(div);
  });
  attachDynEvents();
}

function renderSkillsList() {
  const container = document.getElementById('skillsList');
  container.innerHTML = '';
  state.skills.forEach((sk, i) => {
    const div = document.createElement('div');
    div.className = 'skill-chip';
    div.innerHTML = `
      <div style="flex:1">
        <div style="display:flex;justify-content:space-between;font-size:12px;margin-bottom:3px">
          <span>${sk.name}</span><span style="color:var(--text-muted)">${sk.level}%</span>
        </div>
        <div class="skill-chip-bar"><div class="skill-chip-fill" style="width:${sk.level}%"></div></div>
      </div>
      <button class="remove-btn" data-i="${i}" data-type="skills" style="position:static;margin-left:8px"><i class="fas fa-times"></i></button>
    `;
    container.appendChild(div);
  });
  attachDynEvents();
}

function renderLanguagesList() {
  const container = document.getElementById('languagesList');
  container.innerHTML = '';
  state.languages.forEach((lang, i) => {
    const div = document.createElement('div');
    div.className = 'skill-chip';
    div.innerHTML = `
      <span style="font-size:12px;flex:1">${lang.name} <span style="color:var(--text-muted)">— ${lang.level}</span></span>
      <button class="remove-btn" data-i="${i}" data-type="languages" style="position:static;margin-left:8px"><i class="fas fa-times"></i></button>
    `;
    container.appendChild(div);
  });
  attachDynEvents();
}

function renderReferencesList() {
  const container = document.getElementById('referencesList');
  container.innerHTML = '';
  state.references.forEach((ref, i) => {
    const div = document.createElement('div');
    div.className = 'dyn-item';
    div.innerHTML = `
      <button class="remove-btn" data-i="${i}" data-type="references"><i class="fas fa-times"></i></button>
      <div class="dyn-label">Nombre</div>
      <input type="text" placeholder="Luis Fernando Marín" value="${ref.name}" data-field="name" data-i="${i}" data-type="references"/>
      <div class="dyn-label">Ocupación</div>
      <input type="text" placeholder="Ingeniero" value="${ref.role}" data-field="role" data-i="${i}" data-type="references"/>
      <div class="dyn-label">Teléfono / Ciudad</div>
      <input type="text" placeholder="314-0000000 · Bogotá" value="${ref.contact}" data-field="contact" data-i="${i}" data-type="references"/>
    `;
    container.appendChild(div);
  });
  attachDynEvents();
}

function attachDynEvents() {
  // Remove buttons
  document.querySelectorAll('.remove-btn').forEach(btn => {
    btn.onclick = () => {
      const type = btn.dataset.type;
      const i = parseInt(btn.dataset.i);
      state[type].splice(i, 1);
      refreshList(type);
      renderCV();
    };
  });
  // Dynamic inputs
  document.querySelectorAll('[data-field][data-type]').forEach(el => {
    el.oninput = () => {
      const type = el.dataset.type;
      const i = parseInt(el.dataset.i);
      const field = el.dataset.field;
      state[type][i][field] = el.value;
      renderCV();
    };
  });
}

function refreshList(type) {
  const map = {
    education: renderEducationList,
    experience: renderExperienceList,
    skills: renderSkillsList,
    languages: renderLanguagesList,
    references: renderReferencesList,
  };
  if (map[type]) map[type]();
}

// ══════════════════════════════════════════════════
//  BOTONES PRINCIPALES
// ══════════════════════════════════════════════════
function setupButtons() {
  document.getElementById('demoBtn').onclick = fillDemo;
  document.getElementById('clearBtn').onclick = clearAll;
  document.getElementById('printBtn').onclick = () => window.print();
}

function fillDemo() {
  Object.assign(state, JSON.parse(JSON.stringify(DEMO)));
  // Sync inputs
  const set = (id, val) => { const el=document.getElementById(id); if(el) el.value=val; };
  set('nameInput', state.name);
  set('jobInput', state.job);
  set('aboutInput', state.about);
  set('phoneInput', state.phone);
  set('emailInput', state.email);
  set('cityInput', state.city);
  set('linkedinInput', state.linkedin);
  renderEducationList();
  renderExperienceList();
  renderSkillsList();
  renderLanguagesList();
  renderReferencesList();
  renderCV();
}

function clearAll() {
  state = {
    template: state.template,
    accent: state.accent,
    name:'', job:'', about:'', photo:null,
    phone:'', email:'', city:'', linkedin:'',
    education:[], experience:[], skills:[], languages:[], references:[],
  };
  ['nameInput','jobInput','aboutInput','phoneInput','emailInput','cityInput','linkedinInput'].forEach(id => {
    const el=document.getElementById(id); if(el) el.value='';
  });
  const thumb=document.getElementById('photoPreviewThumb');
  const ph=document.getElementById('photoPlaceholder');
  if(thumb){thumb.src='';thumb.style.display='none';}
  if(ph) ph.style.display='flex';
  renderEducationList();
  renderExperienceList();
  renderSkillsList();
  renderLanguagesList();
  renderReferencesList();
  renderCV();
}

// ══════════════════════════════════════════════════
//  ZOOM
// ══════════════════════════════════════════════════
function setupZoom() {
  document.getElementById('zoomIn').onclick = () => { zoom=Math.min(zoom+10,150); applyZoom(); };
  document.getElementById('zoomOut').onclick = () => { zoom=Math.max(zoom-10,40); applyZoom(); };
  applyZoom();
}
function applyZoom() {
  document.getElementById('cv').style.transform = `scale(${zoom/100})`;
  document.getElementById('zoomLevel').textContent = zoom+'%';
  const wrapper = document.getElementById('cvWrapper');
  const scale = zoom/100;
  wrapper.style.minHeight = `${1123*scale + 64}px`;
}

// ══════════════════════════════════════════════════
//  RENDER PRINCIPAL
// ══════════════════════════════════════════════════
function renderCV() {
  const cv = document.getElementById('cv');
  cv.className = `cv template-${state.template}`;

  const ac = state.accent;
  const acRgb = hexToRgb(ac);
  const acLight = `rgba(${acRgb},0.15)`;
  const acMed = `rgba(${acRgb},0.3)`;

  let html = '';

  if (state.template === 'dark') html = renderDark(ac, acLight, acMed);
  else if (state.template === 'light') html = renderLight(ac, acLight, acMed);
  else if (state.template === 'creative') html = renderCreative(ac, acLight, acMed);
  else if (state.template === 'minimal') html = renderMinimal(ac, acLight, acMed);

  cv.innerHTML = html;
}

// ══════════════════════════════════════════════════
//  HELPERS HTML
// ══════════════════════════════════════════════════
const esc = s => (s||'').replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;');
const ph = (val, fallback) => esc(val) || `<span style="opacity:0.3">${fallback}</span>`;

function photoTag(cls, size='round') {
  if (state.photo) {
    if(size==='square') return `<img src="${state.photo}" style="width:100%;height:100%;object-fit:cover"/>`;
    return `<img src="${state.photo}" style="width:100%;height:100%;object-fit:cover"/>`;
  }
  return `<div class="photo-placeholder"><i class="fas fa-camera"></i></div>`;
}

function hexToRgb(hex) {
  const r = parseInt(hex.slice(1,3),16);
  const g = parseInt(hex.slice(3,5),16);
  const b = parseInt(hex.slice(5,7),16);
  return `${r},${g},${b}`;
}

// ══════════════════════════════════════════════════
//  TEMPLATE DARK
// ══════════════════════════════════════════════════
function renderDark(ac, acLight, acMed) {
  const skillsHtml = state.skills.map(sk => `
    <div class="cv-skill-name"><span>${esc(sk.name)}</span><span style="color:${ac}">${sk.level}%</span></div>
    <div class="cv-skill-bar"><div class="cv-skill-fill" style="width:${sk.level}%;background:linear-gradient(90deg,${ac},${acMed})"></div></div>
  `).join('') || '<span style="opacity:0.3;font-size:11px">Sin habilidades aún</span>';

  const eduHtml = state.education.map(e => `
    <div class="cv-edu-year" style="color:${ac}">${esc(e.year)}</div>
    <div class="cv-edu-title">${esc(e.title)}</div>
    <div class="cv-edu-inst">${esc(e.institution)}</div>
  `).join('') || '<span style="opacity:0.3;font-size:11px">Sin educación aún</span>';

  const langsHtml = state.languages.map(l => `
    <div class="cv-lang-item">
      <span>${esc(l.name)}</span>
      <span class="cv-lang-badge" style="color:${ac};border:1px solid ${acMed}">${esc(l.level)}</span>
    </div>
  `).join('') || '';

  const expHtml = state.experience.map(e => `
    <div class="cv-exp-item">
      <div class="cv-exp-header">
        <div class="cv-exp-company" style="color:${ac}">${esc(e.company)}</div>
        <div class="cv-exp-period">${esc(e.period)}</div>
      </div>
      <div class="cv-exp-role">${esc(e.role)}</div>
      <div class="cv-exp-desc">${esc(e.description)}</div>
    </div>
  `).join('') || '<span style="opacity:0.3;font-size:11px">Sin experiencia aún</span>';

  const refsHtml = state.references.length ? `<div class="cv-ref-grid">${
    state.references.map(r => `
      <div class="cv-ref-item" style="border-left:2px solid ${ac}">
        <div class="cv-ref-name" style="color:${ac}">${esc(r.name)}</div>
        <div class="cv-ref-role">${esc(r.role)}</div>
        <div class="cv-ref-contact"><i class="fas fa-phone" style="font-size:9px;margin-right:4px"></i>${esc(r.contact)}</div>
      </div>
    `).join('')
  }</div>` : '';

  return `
  <div class="cv-sidebar">
    <div class="cv-sidebar-photo">${state.photo ? `<img src="${state.photo}"/>` : '<div class="photo-placeholder" style="width:100%;height:250px;background:linear-gradient(135deg,#1a1f2e,#0d0f14);display:flex;align-items:center;justify-content:center;font-size:60px;color:#333"><i class="fas fa-user"></i></div>'}</div>
    <div class="cv-sidebar-inner">

      <div class="cv-sidebar-section">
        <div class="cv-sidebar-title" style="color:${ac}">Contacto</div>
        ${state.phone?`<div class="cv-contact-item"><i class="fas fa-phone" style="color:${ac}"></i><span>${esc(state.phone)}</span></div>`:''}
        ${state.email?`<div class="cv-contact-item"><i class="fas fa-envelope" style="color:${ac}"></i><span>${esc(state.email)}</span></div>`:''}
        ${state.city?`<div class="cv-contact-item"><i class="fas fa-map-marker-alt" style="color:${ac}"></i><span>${esc(state.city)}</span></div>`:''}
        ${state.linkedin?`<div class="cv-contact-item"><i class="fab fa-linkedin" style="color:${ac}"></i><span>${esc(state.linkedin)}</span></div>`:''}
        ${(!state.phone&&!state.email&&!state.city&&!state.linkedin)?'<span style="opacity:0.3;font-size:11px">Sin contacto aún</span>':''}
      </div>

      ${state.education.length?`
      <div class="cv-sidebar-section">
        <div class="cv-sidebar-title" style="color:${ac}">Educación</div>
        ${eduHtml}
      </div>`:''}

      <div class="cv-sidebar-section">
        <div class="cv-sidebar-title" style="color:${ac}">Habilidades</div>
        ${skillsHtml}
      </div>

      ${state.languages.length?`
      <div class="cv-sidebar-section">
        <div class="cv-sidebar-title" style="color:${ac}">Idiomas</div>
        ${langsHtml}
      </div>`:''}

    </div>
  </div>

  <div class="cv-main">
    <div class="cv-name">${ph(state.name,'NOMBRE APELLIDO')}</div>
    <div class="cv-job" style="color:${ac}">${ph(state.job,'Tu profesión')}</div>
    <div style="width:40px;height:3px;background:${ac};border-radius:2px;margin-bottom:24px"></div>

    <div class="cv-main-section">
      <div class="cv-main-title" style="color:${ac};border-bottom-color:rgba(${hexToRgb(ac)},0.2)">
        <span style="background:${ac};width:16px;height:2px;border-radius:1px;display:inline-block;flex-shrink:0"></span>
        Sobre mí
      </div>
      <div class="cv-about">${ph(state.about,'Aquí aparecerá tu perfil profesional automáticamente.')}</div>
    </div>

    <div class="cv-main-section">
      <div class="cv-main-title" style="color:${ac};border-bottom-color:rgba(${hexToRgb(ac)},0.2)">
        <span style="background:${ac};width:16px;height:2px;border-radius:1px;display:inline-block;flex-shrink:0"></span>
        Experiencia Laboral
      </div>
      ${expHtml}
    </div>

    ${state.references.length?`
    <div class="cv-main-section">
      <div class="cv-main-title" style="color:${ac};border-bottom-color:rgba(${hexToRgb(ac)},0.2)">
        <span style="background:${ac};width:16px;height:2px;border-radius:1px;display:inline-block;flex-shrink:0"></span>
        Referencias Personales
      </div>
      ${refsHtml}
    </div>`:''}
  </div>
  `;
}

// ══════════════════════════════════════════════════
//  TEMPLATE LIGHT
// ══════════════════════════════════════════════════
function renderLight(ac, acLight, acMed) {
  const skillsHtml = state.skills.map(sk => `
    <div class="cv-skill-name"><span>${esc(sk.name)}</span><span style="color:${ac}">${sk.level}%</span></div>
    <div class="cv-skill-bar"><div class="cv-skill-fill" style="width:${sk.level}%;background:${ac}"></div></div>
  `).join('') || '<span style="opacity:0.4;font-size:11px">Sin habilidades</span>';

  const eduHtml = state.education.map(e => `
    <div class="cv-edu-year">${esc(e.year)}</div>
    <div class="cv-edu-title">${esc(e.title)}</div>
    <div class="cv-edu-inst">${esc(e.institution)}</div>
  `).join('') || '';

  const langsHtml = state.languages.map(l => `
    <div class="cv-lang-item">
      <span>${esc(l.name)}</span>
      <span class="cv-lang-badge">${esc(l.level)}</span>
    </div>
  `).join('') || '';

  const expHtml = state.experience.map(e => `
    <div class="cv-exp-item" style="border-left-color:${ac}">
      <div style="position:absolute;left:-5px;top:5px;width:8px;height:8px;border-radius:50%;background:${ac}"></div>
      <div class="cv-exp-header">
        <div class="cv-exp-company">${esc(e.company)}</div>
        <div class="cv-exp-period" style="background:${ac}">${esc(e.period)}</div>
      </div>
      <div class="cv-exp-role">${esc(e.role)}</div>
      <div class="cv-exp-desc">${esc(e.description)}</div>
    </div>
  `).join('') || '<span style="opacity:0.3;font-size:12px">Sin experiencia aún</span>';

  const refsHtml = state.references.map(r => `
    <div class="cv-ref-item" style="border-left-color:${ac}">
      <div class="cv-ref-name" style="color:#1a1a3e">${esc(r.name)}</div>
      <div class="cv-ref-role">${esc(r.role)}</div>
      <div class="cv-ref-contact">${esc(r.contact)}</div>
    </div>
  `).join('');

  return `
  <div class="cv-sidebar">
    <div class="cv-sidebar-photo">
      ${state.photo ? `<img src="${state.photo}" style="width:130px;height:130px;object-fit:cover;border-radius:50%;border:4px solid rgba(255,255,255,0.2)"/>` : '<div class="photo-placeholder" style="width:130px;height:130px;border-radius:50%;background:rgba(255,255,255,0.1);display:flex;align-items:center;justify-content:center;font-size:40px;color:rgba(255,255,255,0.3);border:3px solid rgba(255,255,255,0.15)"><i class="fas fa-user"></i></div>'}
    </div>
    <div class="cv-sidebar-inner">
      <div class="cv-sidebar-section">
        <div class="cv-sidebar-title">Contacto</div>
        ${state.phone?`<div class="cv-contact-item"><i class="fas fa-phone" style="color:${ac}"></i>${esc(state.phone)}</div>`:''}
        ${state.email?`<div class="cv-contact-item"><i class="fas fa-envelope" style="color:${ac}"></i>${esc(state.email)}</div>`:''}
        ${state.city?`<div class="cv-contact-item"><i class="fas fa-map-marker-alt" style="color:${ac}"></i>${esc(state.city)}</div>`:''}
        ${state.linkedin?`<div class="cv-contact-item"><i class="fab fa-linkedin" style="color:${ac}"></i>${esc(state.linkedin)}</div>`:''}
      </div>
      ${state.education.length?`<div class="cv-sidebar-section"><div class="cv-sidebar-title">Educación</div>${eduHtml}</div>`:''}
      <div class="cv-sidebar-section"><div class="cv-sidebar-title">Habilidades</div>${skillsHtml}</div>
      ${state.languages.length?`<div class="cv-sidebar-section"><div class="cv-sidebar-title">Idiomas</div>${langsHtml}</div>`:''}
    </div>
  </div>

  <div class="cv-main">
    <div class="cv-name" style="color:#1a1a3e">${ph(state.name,'NOMBRE APELLIDO')}</div>
    <div class="cv-job">${ph(state.job,'Tu profesión')}</div>
    <div class="cv-accent-line" style="background:${ac};width:50px;height:3px;border-radius:2px;margin-bottom:20px"></div>

    <div class="cv-main-section">
      <div class="cv-main-title">
        <span style="background:${ac};width:12px;height:3px;border-radius:1px;display:inline-block;flex-shrink:0"></span>
        Sobre mí
      </div>
      <div class="cv-about">${ph(state.about,'Tu perfil profesional aparecerá aquí.')}</div>
    </div>

    <div class="cv-main-section">
      <div class="cv-main-title">
        <span style="background:${ac};width:12px;height:3px;border-radius:1px;display:inline-block;flex-shrink:0"></span>
        Experiencia Laboral
      </div>
      ${expHtml}
    </div>

    ${state.references.length?`
    <div class="cv-main-section">
      <div class="cv-main-title">
        <span style="background:${ac};width:12px;height:3px;border-radius:1px;display:inline-block;flex-shrink:0"></span>
        Referencias
      </div>
      <div class="cv-ref-grid">${refsHtml}</div>
    </div>`:''}
  </div>
  `;
}

// ══════════════════════════════════════════════════
//  TEMPLATE CREATIVE
// ══════════════════════════════════════════════════
function renderCreative(ac, acLight, acMed) {
  const chips = [state.phone, state.email, state.city].filter(Boolean).map(v =>
    `<div class="cv-header-chip"><i class="fas fa-circle" style="font-size:5px;color:${ac}"></i>${esc(v)}</div>`
  ).join('');

  const expHtml = state.experience.map(e => `
    <div class="cv-exp-item" style="border-left-color:${ac}">
      <div class="cv-exp-header">
        <div class="cv-exp-company" style="color:${ac}">${esc(e.company)}</div>
        <div class="cv-exp-period">${esc(e.period)}</div>
      </div>
      <div class="cv-exp-role">${esc(e.role)}</div>
      <div class="cv-exp-desc">${esc(e.description)}</div>
    </div>
  `).join('') || '<span style="opacity:0.3;font-size:11px">Sin experiencia aún</span>';

  const skillsHtml = state.skills.map(sk => `
    <div class="cv-skill-name"><span>${esc(sk.name)}</span><span style="color:${ac}">${sk.level}%</span></div>
    <div class="cv-skill-bar"><div class="cv-skill-fill" style="width:${sk.level}%;background:linear-gradient(90deg,${ac},${acMed})"></div></div>
  `).join('') || '';

  const eduHtml = state.education.map(e => `
    <div class="cv-edu-year" style="color:${ac}">${esc(e.year)}</div>
    <div class="cv-edu-title">${esc(e.title)}</div>
    <div class="cv-edu-inst">${esc(e.institution)}</div>
  `).join('') || '';

  const refsHtml = state.references.map(r => `
    <div class="cv-ref-item" style="border-left-color:${ac}">
      <div class="cv-ref-name" style="color:${ac}">${esc(r.name)}</div>
      <div class="cv-ref-role">${esc(r.role)}</div>
      <div class="cv-ref-contact">${esc(r.contact)}</div>
    </div>
  `).join('');

  const langsHtml = state.languages.map(l => `
    <div class="cv-lang-item"><span>${esc(l.name)}</span><span class="cv-lang-badge" style="color:${ac}">${esc(l.level)}</span></div>
  `).join('');

  return `
  <div class="cv-header-band">
    <div class="cv-header-content">
      <div class="cv-photo-wrap">
        ${state.photo ? `<img src="${state.photo}" style="width:110px;height:110px;object-fit:cover;border-radius:16px;border:3px solid ${acMed}"/>` : '<div class="photo-placeholder" style="width:110px;height:110px;border-radius:16px;background:rgba(255,255,255,0.05);display:flex;align-items:center;justify-content:center;font-size:36px;color:rgba(255,255,255,0.2);border:3px solid rgba(255,255,255,0.08)"><i class="fas fa-user"></i></div>'}
      </div>
      <div>
        <div class="cv-name" style="background:linear-gradient(135deg,#fff,${ac});-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text">${ph(state.name,'NOMBRE APELLIDO')}</div>
        <div class="cv-job">${ph(state.job,'Tu profesión')}</div>
        <div class="cv-header-chips">${chips}</div>
      </div>
    </div>
  </div>

  <div class="cv-body">
    <div class="cv-main">
      <div class="cv-main-section">
        <div class="cv-main-title" style="color:${ac};border-bottom-color:rgba(${hexToRgb(ac)},0.15)">
          <span style="background:${ac};width:20px;height:2px;border-radius:1px;display:inline-block;flex-shrink:0"></span>
          Sobre mí
        </div>
        <div class="cv-about">${ph(state.about,'Tu perfil profesional aparecerá aquí.')}</div>
      </div>

      <div class="cv-main-section">
        <div class="cv-main-title" style="color:${ac};border-bottom-color:rgba(${hexToRgb(ac)},0.15)">
          <span style="background:${ac};width:20px;height:2px;border-radius:1px;display:inline-block;flex-shrink:0"></span>
          Experiencia Laboral
        </div>
        ${expHtml}
      </div>

      ${state.references.length?`
      <div class="cv-main-section">
        <div class="cv-main-title" style="color:${ac};border-bottom-color:rgba(${hexToRgb(ac)},0.15)">
          <span style="background:${ac};width:20px;height:2px;border-radius:1px;display:inline-block;flex-shrink:0"></span>
          Referencias
        </div>
        ${refsHtml}
      </div>`:''}
    </div>

    <div class="cv-sidebar">
      <div class="cv-sidebar-section">
        <div class="cv-sidebar-title">Habilidades</div>
        ${skillsHtml || '<span style="opacity:0.3;font-size:11px">Sin habilidades</span>'}
      </div>
      ${state.education.length?`<div class="cv-sidebar-section"><div class="cv-sidebar-title">Educación</div>${eduHtml}</div>`:''}
      ${state.languages.length?`<div class="cv-sidebar-section"><div class="cv-sidebar-title">Idiomas</div>${langsHtml}</div>`:''}
    </div>
  </div>
  `;
}

// ══════════════════════════════════════════════════
//  TEMPLATE MINIMAL
// ══════════════════════════════════════════════════
function renderMinimal(ac, acLight, acMed) {
  const skillsHtml = state.skills.map(sk =>
    `<span class="cv-skill-tag" style="border-left:3px solid ${ac}">${esc(sk.name)}</span>`
  ).join('') || '<span style="opacity:0.3;font-size:12px">Sin habilidades</span>';

  const eduHtml = state.education.map(e => `
    <div class="cv-edu-year">${esc(e.year)}</div>
    <div class="cv-edu-title">${esc(e.title)}</div>
    <div class="cv-edu-inst">${esc(e.institution)}</div>
  `).join('') || '';

  const expHtml = state.experience.map(e => `
    <div class="cv-exp-item">
      <div class="cv-exp-header">
        <div class="cv-exp-company">${esc(e.company)}</div>
        <div class="cv-exp-period">${esc(e.period)}</div>
      </div>
      <div class="cv-exp-role" style="color:${ac}">${esc(e.role)}</div>
      <div class="cv-exp-desc">${esc(e.description)}</div>
    </div>
  `).join('') || '<span style="opacity:0.3;font-size:12px">Sin experiencia aún</span>';

  const refsHtml = state.references.map(r => `
    <div class="cv-ref-item">
      <div class="cv-ref-name">${esc(r.name)}</div>
      <div class="cv-ref-role">${esc(r.role)}</div>
      <div class="cv-ref-contact">${esc(r.contact)}</div>
    </div>
  `).join('');

  const langsHtml = state.languages.map(l => `
    <div class="cv-lang-item"><span>${esc(l.name)}</span><span class="cv-lang-badge">${esc(l.level)}</span></div>
  `).join('');

  return `
  <div class="cv-top-bar" style="background:${ac}"></div>
  <div class="cv-header">
    <div class="cv-photo-wrap">
      ${state.photo ? `<img src="${state.photo}" style="width:80px;height:80px;object-fit:cover;border-radius:50%;filter:grayscale(20%)"/>` : '<div class="photo-placeholder" style="width:80px;height:80px;border-radius:50%;background:#eee;display:flex;align-items:center;justify-content:center;font-size:28px;color:#bbb"><i class="fas fa-user"></i></div>'}
    </div>
    <div>
      <div class="cv-name">${ph(state.name,'Nombre Apellido')}</div>
      <div class="cv-job">${ph(state.job,'Tu profesión')}</div>
    </div>
  </div>

  <div class="cv-body">
    <div class="cv-main">
      <div class="cv-main-section">
        <div class="cv-main-title">Sobre mí</div>
        <div class="cv-about">${ph(state.about,'Tu perfil profesional aquí.')}</div>
      </div>
      <div class="cv-main-section">
        <div class="cv-main-title">Experiencia</div>
        ${expHtml}
      </div>
      <div class="cv-main-section">
        <div class="cv-main-title">Habilidades</div>
        <div>${skillsHtml}</div>
      </div>
      ${state.references.length?`<div class="cv-main-section"><div class="cv-main-title">Referencias</div>${refsHtml}</div>`:''}
    </div>
    <div class="cv-sidebar">
      <div class="cv-sidebar-section">
        <div class="cv-sidebar-title">Contacto</div>
        ${state.phone?`<div class="cv-contact-item"><i class="fas fa-phone" style="color:${ac}"></i>${esc(state.phone)}</div>`:''}
        ${state.email?`<div class="cv-contact-item"><i class="fas fa-envelope" style="color:${ac}"></i>${esc(state.email)}</div>`:''}
        ${state.city?`<div class="cv-contact-item"><i class="fas fa-map-marker-alt" style="color:${ac}"></i>${esc(state.city)}</div>`:''}
        ${state.linkedin?`<div class="cv-contact-item"><i class="fab fa-linkedin" style="color:${ac}"></i>${esc(state.linkedin)}</div>`:''}
      </div>
      ${state.education.length?`<div class="cv-sidebar-section"><div class="cv-sidebar-title">Educación</div>${eduHtml}</div>`:''}
      ${state.languages.length?`<div class="cv-sidebar-section"><div class="cv-sidebar-title">Idiomas</div>${langsHtml}</div>`:''}
    </div>
  </div>
  `;
}
