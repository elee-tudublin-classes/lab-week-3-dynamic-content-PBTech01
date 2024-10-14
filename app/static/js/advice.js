document.addEventListener("DOMContentLoaded", function() {
    const adviceText = document.getElementById('advice-text');
    const newAdviceBtn = document.getElementById('new-advice-btn');

    // Function to fetch advice from API
    function fetchAdvice() {
        fetch('https://api.adviceslip.com/advice')
            .then(response => response.json())
            .then(data => {
                adviceText.innerText = data.slip.advice;
            })
            .catch(error => {
                adviceText.innerText = "Failed to fetch advice. Please try again.";
                console.error("Error fetching advice:", error);
            });
    }

    // Fetch initial advice when page loads
    fetchAdvice();

    // Fetch new advice on button click
    newAdviceBtn.addEventListener('click', fetchAdvice);
});