document.addEventListener("DOMContentLoaded", () => {
   let parent = document.getElementById("our-story-logo");
   let logo_a = document.createElement('a');
   logo_a.setAttribute('href', '/kr');
   logo_a.setAttribute('class', 'logo-a');
   parent.parentNode.insertBefore(logo_a, parent);
   logo_a.appendChild(parent);
});

