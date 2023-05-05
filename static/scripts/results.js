
allTD = document.getElementsByTagName('td');

for (td of allTD) {
  if (td.innerHTML.slice(0, 5) == 'https') {

    console.log(td.innerHTML);
    link = td.innerHTML;

    newITEM = document.createElement('a');
    newITEM.target="_blank";
    newITEM.href = link;
    newITEM.innerHTML = 'Go to post';
    newITEM.className = 'post_ref'
    td.innerHTML = '';

    td.appendChild(newITEM);
  }

}