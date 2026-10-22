/* Products available in the store */
const products = [
  {
    name: "Carton of Cherries",
    price: 4,
    quantity: 0,
    productId: 1,
    image: "images/cherry.jpg"
  },
  {
    name: "Bag of Oranges",
    price: 10,
    quantity: 0,
    productId: 2,
    image: "images/orange.jpg"
  },
  {
    name: "Carton of Strawberries",
    price: 5,
    quantity: 0,
    productId: 3,
    image: "images/strawberry.jpg"
  }
];

/* Images provided in /images folder. All images from Unsplash.com
   - cherry.jpg by Mae Mu
   - orange.jpg by Mae Mu
   - strawberry.jpg by Allec Gomes
*/

/* Products currently in the cart */
const cart = [];

/* Total cash received from the customer for the current purchase */
let totalPaid = 0;

/* Returns the product with the given productId from the given list */
function getProductById(productId, productList) {
  return productList.find((product) => product.productId === productId);
}

/* Adds a product to the cart, or increases its quantity if already there */
function addProductToCart(productId) {
  const product = getProductById(productId, products);
  product.quantity += 1;

  if (!cart.includes(product)) {
    cart.push(product);
  }
}

/* Increases the quantity of a product in the cart */
function increaseQuantity(productId) {
  const product = getProductById(productId, cart);
  product.quantity += 1;
}

/* Decreases the quantity of a product, removing it from the cart at 0 */
function decreaseQuantity(productId) {
  const product = getProductById(productId, cart);
  product.quantity -= 1;

  if (product.quantity === 0) {
    removeProductFromCart(productId);
  }
}

/* Removes a product from the cart and resets its quantity */
function removeProductFromCart(productId) {
  const product = getProductById(productId, cart);
  product.quantity = 0;
  cart.splice(cart.indexOf(product), 1);
}

/* Returns the total cost of all products in the cart */
function cartTotal() {
  let total = 0;

  cart.forEach((product) => {
    total += product.price * product.quantity;
  });

  return total;
}

/* Removes all products from the cart */
function emptyCart() {
  cart.forEach((product) => {
    product.quantity = 0;
  });
  cart.length = 0;
}

/* Receives a cash payment and returns the difference from the cart total
   - negative: remaining balance still owed by the customer
   - positive or zero: change to be returned to the customer
   Once the purchase is fully paid, the payment and the cart are reset
*/
function pay(amount) {
  totalPaid += amount;
  const remainingBalance = totalPaid - cartTotal();

  if (remainingBalance >= 0) {
    totalPaid = 0;
    emptyCart();
  }

  return remainingBalance;
}

module.exports = {
  products,
  cart,
  addProductToCart,
  increaseQuantity,
  decreaseQuantity,
  removeProductFromCart,
  cartTotal,
  pay,
  emptyCart
};
