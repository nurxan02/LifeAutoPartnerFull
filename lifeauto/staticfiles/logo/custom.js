const versionDiv = document.querySelector("div.float-right.d-none.d-sm-inline");
if (versionDiv) {
  versionDiv.innerHTML = `
        <a href="https://nurxan02.github.io/MyPortfolio" 
           target="_blank" 
           style="color:rgb(222, 169, 24); text-decoration: none;">
            <i class="fab fa-waspp"></i> Developer by Nurkhan Masimzada
        </a>

    `;
}
const brandText = document.querySelector(".brand-text.font-weight-light");

if (brandText) {
  brandText.classList.remove("font-weight-light");
  brandText.classList.add("font-weight-bold");
}
(function () {
  const headers = document.querySelectorAll("li.nav-header");

  headers.forEach((header) => {
    if (header.textContent.trim()) {
      header.classList.add("navHeaderCustom");
    }
  });
})();
