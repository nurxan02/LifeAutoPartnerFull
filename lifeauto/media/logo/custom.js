const versionDiv = document.querySelector("div.float-right.d-none.d-sm-inline");
if (versionDiv) {
  versionDiv.innerHTML = `
        <a href="https://bio.link/nurxanmasimzade" 
           target="_blank" 
           style="color:rgb(222, 169, 24); text-decoration: none;">
            <i class="fab fa-waspp"></i> Developer by Nurkhan Masimzada
        </a>

    `;
}
const brandText = document.querySelector(".brand-text.font-weight-light");

if (brandText) {
  // Remove the light class and add bold class
  brandText.classList.remove("font-weight-light");
  brandText.classList.add("font-weight-bold");
}
