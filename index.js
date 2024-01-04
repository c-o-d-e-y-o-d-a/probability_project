function sd() {
  fetch("http://127.0.0.1:5000/home/TSLA")
    .then((response) => response.blob())
    .then((data) => {
      displayImage(data);
    })
    .catch((error) => console.error("FETCH ERROR:", error));
}

function displayImage(imageBlob) {
  const imgDiv = document.querySelector(".image-container");
  const imageUrl = URL.createObjectURL(imageBlob);

  // Clear existing images before appending a new one
  imgDiv.innerHTML = "";

  const imgElement = document.createElement("img");
  imgElement.src = imageUrl;

  imgDiv.appendChild(imgElement);
}

// Attach the sd function to the button click event
document.addEventListener('DOMContentLoaded', function() {
  const button1 = document.getElementById('butt');
  button1.addEventListener('click', sd);
});

function myData() {
  retrun;
}

function show() {
  document.getElementById('anotherFunction').classList.toggle('Active');
}
