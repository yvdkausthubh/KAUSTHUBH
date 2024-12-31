// Function to toggle the visibility of answers
function toggleAnswer(id) {
    const answer = document.getElementById(id);
    answer.style.display = answer.style.display === 'block' ? 'none' : 'block';
}

// Smooth Scroll for navigation
document.querySelectorAll('nav a').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();

        document.querySelector(this.getAttribute('href')).scrollIntoView({
            behavior: 'smooth'
        });
    });
});
