// Aqua particle animation - slow, blurred, semi-transparent
const canvas = document.getElementById("particle-canvas");
const ctx = canvas.getContext("2d");

canvas.width = window.innerWidth;
canvas.height = window.innerHeight;

let particles = [];

function initParticles() {
    particles = [];
    for (let i = 0; i < 80; i++) {
        particles.push({
            x: Math.random() * canvas.width,
            y: Math.random() * canvas.height,
            radius: Math.random() * 3 + 2,
            dx: (Math.random() - 0.5) * 0.4, // slower movement
            dy: (Math.random() - 0.5) * 0.4,
            blur: Math.random() * 20 + 15,
            opacity: Math.random() * 0.5 + 0.2 // softer glow
        });
    }
}

function drawParticles() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    particles.forEach(p => {
        ctx.beginPath();
        ctx.arc(p.x, p.y, p.radius, 0, Math.PI * 2);
        ctx.fillStyle = `rgba(0, 255, 255, ${p.opacity})`;
        ctx.shadowColor = "aqua";
        ctx.shadowBlur = p.blur;
        ctx.fill();

        // Move slowly
        p.x += p.dx;
        p.y += p.dy;

        // Bounce off edges
        if (p.x < 0 || p.x > canvas.width) p.dx *= -1;
        if (p.y < 0 || p.y > canvas.height) p.dy *= -1;
    });
}

function animate() {
    drawParticles();
    requestAnimationFrame(animate);
}

initParticles();
animate();

// Resize handler
window.addEventListener("resize", () => {
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;
    initParticles();
});
