const calendar = document.querySelector(".calendar"),
    date = document.querySelector(".date"),
    daysContainer = document.querySelector(".days"),
    prev = document.querySelector(".prev");
        next = document.querySelector(".next");


        let today = new Date();
        let activeDay;
        let month = today.getFullMonth();
        let year = today.getFullYear();


// 20 MINS YTB