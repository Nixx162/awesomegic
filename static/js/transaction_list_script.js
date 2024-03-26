const list = document.querySelector('.transaction-list');
const currPage = document.querySelector('#current-page');
const totalPages = document.querySelector('#total-pages');
const buttonPrev = document.querySelector('#prev-page');
const buttonNext = document.querySelector('#next-page');

const items = JSON.parse(
  document.currentScript.nextElementSibling.textContent
);
let currentPage = 1;
let currentIndex = 0;
const itemsPerPage = 5;

const numPages = Math.max(1, Math.ceil(items.length / itemsPerPage));

// Functions
const createListItem = (item) => {
  if (item.transaction_type == "Deposit") {
    return `<li class="list-item-deposit"><h4 class="item-title">${item.transaction_type}</h4><p>$${item.value}</p></li>`;
  } else {
    return `<li class="list-item-withdraw"><h4 class="item-title">${item.transaction_type}</h4><p>-$${item.value}</p></li>`;
  }
  
}

const nextPage = () => {
  if (currentPage === numPages) return;

  currentPage++;
  currentIndex = (currentPage - 1) * itemsPerPage;
  let newIndex = currentIndex + itemsPerPage;
  list.innerHTML = items
    .slice(currentIndex, newIndex)
    .map((item) => createListItem(item))
    .join('');
  currPage.innerHTML = currentPage;
};

const prevPage = () => {
  if (currentPage === 1) return;

  currentPage--;
  currentIndex = (currentPage - 1) * itemsPerPage;
  let newIndex = currentIndex + itemsPerPage;
  list.innerHTML = items
    .slice(currentIndex, newIndex)
    .map((item) => createListItem(item))
    .join('');
  currPage.innerHTML = currentPage;
};

const init = () => {
  currPage.innerHTML = currentPage;
  totalPages.innerHTML = numPages;

  list.innerHTML = items
    .slice(0, itemsPerPage)
    .map((item) => createListItem(item))
    .join('');
};

// Event Listeners
buttonPrev.addEventListener('click', prevPage);
buttonNext.addEventListener('click', nextPage);

init();