let button = document.getElementById("submit");
let div = document.getElementById("div");
let flavor = document.getElementById("flavor");
let size = document.getElementById("size");
let rating = document.getElementById("rating");
let image = document.getElementById("image");

$('.delete-cupcake').click(deleteCupcake)

async function makeCupcake(e) {
  e.preventDefault(); 
  try {
    const response = await axios.post("/api/cupcakes", {
      flavor: flavor.value,
      size: size.value,
      rating: rating.value,
      image: image.value
    });
    let cupcakeLi = document.createElement("li"); 
    cupcakeLi.textContent = `${response.data.cupcake.flavor} - Size ${response.data.cupcake.size} - Rating: ${response.data.cupcake.rating} -Image ${response.data.cupcake.image}`; // Set the text content
    document.querySelector("ul").appendChild(cupcakeLi); 
  } catch (error) {
    console.error(error); 
  }
}

button.addEventListener("click", makeCupcake);
