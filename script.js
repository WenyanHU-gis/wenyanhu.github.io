fetch('portfolio.json')
  .then(response => response.json())
  .then(data => {
    
    document.getElementById('name').innerText = data.profile.name;
    document.getElementById('summary').innerText = data.summary;

    const projectHTML = data.projects.map(p => `
      <div class="project">
        <h3>${p.name}</h3>
        <p>${p.description}</p>
        <p><b>Tech:</b> ${p.technologies.join(', ')}</p>
        <a href="${p.github}" target="_blank">GitHub Repo</a>
      </div>
    `).join('');

    document.getElementById('projects').innerHTML = projectHTML;

  });
