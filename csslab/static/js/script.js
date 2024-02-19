// function that changes the background color
function changeBackgroundColor() {
    // create random values for rgb 
    var r = Math.floor(Math.random() * 256);
    var g = Math.floor(Math.random() * 256);
    var b = Math.floor(Math.random() * 256);

    // create a rgb color string
    var color = 'rgb(' + r + ',' + g + ',' + b + ')';

    // update the background color to the newly calculated rgb value
    document.body.style.backgroundColor = color;
}

