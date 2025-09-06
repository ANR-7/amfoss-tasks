
const canvas = document.getElementById("drawCanvas");
const ctx = canvas.getContext("2d");

const message = document.getElementById("message");
const vent = document.getElementById("vent")
const vict = document.getElementById("vict")

var highscore = 0;

// If highscore alr exists
let saved = sessionStorage.getItem("highscore")
if (saved) highscore = Number(saved);

canvas.width = window.innerWidth;
canvas.height = window.innerHeight;

let drawing = false;

canvas.addEventListener("mousedown", () => {
    
    drawing = true;
    currentStroke = []
    ctx.beginPath();

    ctx.clearRect(0, 0, canvas.width, canvas.height);
});

canvas.addEventListener("mouseup", () => {
    if (score() > highscore){
        highscore = score()

        // Session storage
        sessionStorage.setItem("highscore", highscore);

        // Avoids audio clash during highscore
        vent.pause()
        vict.play()

    }    
    drawing = false;
    // Make it a closed polygon
    currentStroke.push(currentStroke[0])

    if (!pointInPolygon(currentStroke)){

        message.textContent = "Red dot aint in your circle twin";
        vent.currentTime=3;
        // Audio clash is fine during vent imo
        vent.play()

    }

    else {
        if (isNaN(score())){
            message.innerHTML="Hi"
        }
        else{
            message.innerHTML = score().toFixed(2)+"% <br/>";
            message.innerHTML += "Highscore is "+highscore.toFixed(2);
            console.log(highscore)
        }

    }
});

canvas.addEventListener("mousemove", (e) => {
    if (!drawing) return;

    ctx.lineWidth = 10;
    // ctx.lineCap = "round";
    ctx.strokeStyle = "red";

    ctx.lineTo(e.offsetX, e.offsetY);
    ctx.stroke();
    ctx.beginPath();
    ctx.moveTo(e.offsetX, e.offsetY);
    
    // Get an array of points
    addPoint(e)
    // Get their centroid
});

// Helper functions

function addPoint(e) {
  currentStroke.push({ x: e.offsetX, y: e.offsetY });
}

function pointInPolygon(polygon) {
  let px = canvas.width/2
  let py = canvas.height/2
  let inside = false;

  for (let i = 0, j = polygon.length - 1; i < polygon.length; j = i++) {
    let xi = polygon[i].x;
    let yi = polygon[i].y;
    let xj = polygon[j].x;
    let yj = polygon[j].y;

    // check if the edge crosses the horizontal line at y = py
    let intersects = ((yi > py) !== (yj > py)) &&
                     (px < (xj - xi) * (py - yi) / (yj - yi) + xi);

    if (intersects) {
      inside = !inside; // flip between true and false
    }
  }

  return inside;
}

function score(){
    let x = 0;
    let y = 0;
    for (let i=0; i<currentStroke.length; i++){
        x+=currentStroke[i].x;
        y+=currentStroke[i].y;
    }

    centroid = {x : x/currentStroke.length, y: y/currentStroke.length}

    let distances = []
    let radius = 0;
    // Get total radius and an array of distances
    for (let i=0; i<currentStroke.length; i++){
        d = Math.sqrt((currentStroke[i].x - centroid.x)**2 + (currentStroke[i].y - centroid.y)**2)
        radius += d;
        distances.push(d)
    }
    
    radius/= currentStroke.length

    // Deviation kand pidi
    deviation = 0
    for (let d of distances){
        deviation += Math.abs(d - radius)
    }
    deviation/=currentStroke.length


    let score = 100 - (deviation/radius) * 100


    return score;
}
