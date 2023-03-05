const calendar = document.querySelector(".calendar"),
    date = document.querySelector(".date"),
    daysContainer = document.querySelector(".days"),
    prev = document.querySelector(".prev");
    next = document.querySelector(".next");


let today = new Date();
let activeDay;
let month = today.getFullMonth();
let year = today.getFullYear()

const months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
];

//fonction pour ajouter les jours

function initCalendar() {
    const firstDay = new Date(year, month, 1);
    const lastDay = new Date(year, month + 1, 0);
    const prevLastDay = new Date(year, month, 0);
    const prevDays = prevLastDay.getDate();
    const lastDays = lastDay.getDate();
    const day = firstDay.getDate();
    const nextDays = 7 - lastDay.getDay() - 1;

    //mettre a jour la date en haut du calendrier
    date.innerHTML = months[month] + " " + year;

    //ajouter les jours sur le dom
    let days = "";

    //les jours du mois precedent
    for (let x = day; x > 0; x--) {
        days = "<div class='day prev-date'>${prevDays - x + 1}</div>";
    }
    //les jours du mois actuel
    for (let i = 1; i <= lastDays; i++) {
        //si le jour est le jour actuel
        if (i === new Date().getDate() && 
        year === Date().getFullYear() && 
        month === Date().getMonth()
        ) {
            days += '<div class="day today">${i}</div>';
        }
        else {
            days += '<div class="day">${i}</div>';
        }
    }

    //les jours du mois suivant
    for (let j = 1; j <= nextDays; j++) {
        days += '<div class="day next-date">${j}</div>';
    }
    daysContainer.innerHTML = days;
}

initCalendar();

//mois precedent
function prevMonth() {
    month--;
    if (month < 0) {
        month = 11;
        year--;
    }
    initCalendar();
}

//mois suivant
function nextMonth() {
    month++;
    if (month > 11) {
        month = 0;
        year++;
    }
    initCalendar();
}

//ajout d'un eventlistener sur les boutons précédent et suivant
prev.addEventListener("click", prevMonth);
next.addEventListener("click", nextMonth);