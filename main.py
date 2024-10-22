function calculateFinalSpeed(initialSpeed: number, inclinations: number[]): number {
    let currentSpeed = initialSpeed;
    for (let incline of inclinations) {
        if (incline > 0) {
            currentSpeed -= incline;  
        } else if (incline < 0) {
            currentSpeed += Math.abs(incline);  
        }
        
        if (currentSpeed <= 0) {
            return 0;
        }
    }
    return currentSpeed;
}
console.log(calculateFinalSpeed(60, [0, 30, 0, -45, 0])); 
