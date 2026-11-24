let scene, camera, renderer, particles, particleCount = 15000;
let mouseX = 0, mouseY = 0;
let targetX = 0, targetY = 0;

function initThree() {
    scene = new THREE.Scene();
    camera = new THREE.PerspectiveCamera(60, window.innerWidth / window.innerHeight, 1, 4000);
    camera.position.z = 1000;

    renderer = new THREE.WebGLRenderer({ 
        canvas: document.getElementById('three-bg'),
        alpha: true,
        antialias: true 
    });
    renderer.setSize(window.innerWidth, window.innerHeight);
    renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));

    const geometry = new THREE.BufferGeometry();
    const vertices = [];
    const colors = [];
    const color = new THREE.Color();

    for (let i = 0; i < particleCount; i++) {
        vertices.push(
            Math.random() * 4000 - 2000,
            Math.random() * 4000 - 2000,
            Math.random() * 4000 - 2000
        );
        
        // Brighter, more vibrant colors for stars
        const vx = (Math.random() * 0.3) + 0.6;  // Increased red channel
        const vy = (Math.random() * 0.3) + 0.7;  // Increased green channel  
        const vz = (Math.random() * 0.4) + 0.9;  // Increased blue channel
        color.setRGB(vx, vy, vz);
        colors.push(color.r, color.g, color.b);
    }

    geometry.setAttribute('position', new THREE.Float32BufferAttribute(vertices, 3));
    geometry.setAttribute('color', new THREE.Float32BufferAttribute(colors, 3));

    const material = new THREE.PointsMaterial({
        size: 3,  // Increased size
        vertexColors: true,
        transparent: true,
        opacity: 0.8,  // Increased opacity
        sizeAttenuation: true,
        blending: THREE.AdditiveBlending  // Additive blending for brightness
    });

    particles = new THREE.Points(geometry, material);
    scene.add(particles);
}

function animate() {
    requestAnimationFrame(animate);

    // Smooth mouse follow
    targetX = mouseX * 0.05;
    targetY = mouseY * 0.05;

    particles.rotation.x += 0.0005 + (targetY * 0.02);
    particles.rotation.y += 0.0005 + (targetX * 0.02);

    // Subtle floating effect
    const time = Date.now() * 0.00005;
    particles.position.x = Math.sin(time) * 20;
    particles.position.z = Math.cos(time) * 10;

    renderer.render(scene, camera);
}

window.addEventListener('resize', () => {
    camera.aspect = window.innerWidth / window.innerHeight;
    camera.updateProjectionMatrix();
    renderer.setSize(window.innerWidth, window.innerHeight);
});

window.addEventListener('mousemove', (e) => {
    mouseX = (e.clientX - window.innerWidth / 2) / 100;
    mouseY = (e.clientY - window.innerHeight / 2) / 100;
});

document.addEventListener('DOMContentLoaded', () => {
    initThree();
    animate();
});
