function getTime() {
    let now = new Date();

    // return object with date and time in required format
    return {
        date: now.toLocaleDateString('en-ie'),
        time: now.toLocaleTimeString('en-ie')
    };
}

const browserTime = document.getElementById('browserTime');

// Update browser time
function updateBrowserTime() {
    const now = getTime();
    browserTime.innerText = `${now.date} ${now.time}`;
    // Recursive call to update every second
    setTimeout(updateBrowserTime, 1000);
}

// Initialize the time on page load
updateBrowserTime();

