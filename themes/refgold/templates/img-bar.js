
/**
 * Randomize array element order in-place.
 * Using Durstenfeld shuffle algorithm.
 * http://stackoverflow.com/questions/2450954/how-to-randomize-shuffle-a-javascript-array
 */
function shuffleArray(array) {
    for (var i = array.length - 1; i > 0; i--) {
        var j = Math.floor(Math.random() * (i + 1));
        var temp = array[i];
        array[i] = array[j];
        array[j] = temp;
    }
    return array;
}



function makeBar(){
  // Array string is formed in pelicanconf.py
  var imgs = {{ BARIMGSJSON }};

  // The bar will have this many images in it:
  var n = 12;

  shuffleArray(imgs);

  var bar = document.getElementById('random_images');

  var ul = document.createElement('ul');
  while(n--){
    var li = document.createElement('li');
    li.innerHTML = "<img src='" + imgs[n] + "' alt='' />";
    ul.appendChild(li);
  }
  bar.appendChild(ul);
}

makeBar()
