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

document.querySelectorAll(".field-status").forEach((element) => {
  const status = element.textContent.trim();
  switch (status) {
    case "Active":
      element.style.fontWeight = "bold";
      s;
      element.style.color = "rgb(20, 219, 20)";
      element.style.fontSize = "1.2em";
      break;
    case "Deactive":
      element.style.color = "red";
      element.style.fontWeight = "bold";
      element.style.fontSize = "1.2em";
      break;
    case "Pending":
      element.style.color = "yellow";
      element.style.fontWeight = "bold";
      element.style.fontSize = "1.2em";
      break;
    case "Expired":
      element.style.color = "rgb(87, 87, 255)";
      element.style.fontWeight = "bold";
      element.style.fontSize = "1.2em";
      break;
  }
});
