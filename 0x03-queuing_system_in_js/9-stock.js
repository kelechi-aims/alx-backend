const express = require('express');
const redis = require('redis');
import { promisify } from 'util';

// Create an Express server
const app = express();
const port = 1245;

app.use(express.json());

// Create an array listProducts containing the list of products
const listProducts = [
  {
    itemId: 1,
    itemName: 'Suitcase 250',
    price: 50,
    initialAvailableQuantity: 4,
  },
  {
    itemId: 2,
    itemName: 'Suitcase 450',
    price: 100,
    initialAvailableQuantity: 10,
  },
  {
    itemId: 3,
    itemName: 'Suitcase 650',
    price: 350,
    initialAvailableQuantity: 2,
  },
  {
    itemId: 4,
    itemName: 'Suitcase 1050',
    price: 550,
    initialAvailableQuantity: 5,
  },
];

// Implement getItemById function
function getItemById(id) {
  return listProducts.find((item) => item.itemId === id);
}

// Create route GET /list_products
app.get('/list_products', (req, res) => {
  res.json(listProducts);
});

// Create a Redis client
const client = redis.createClient();

// Function to reserve stock by itemId in Redis
function reserveStockById(itemId, stock) {
  client.set(`item.${itemId}`, stock);
}

// Promisify Redis commands
const getAsync = promisify(client.get).bind(client);

// Function to get the current reserved stock by itemId from Redis
async function getCurrentReservedStockById(itemId) {
  const stock = await getAsync(`item.${itemId}`);
  return stock;
}

app.get('/list_products/:itemId', async (req, res) => {
  const itemId = Number(req.params.itemId);
  const item = getItemById(itemId);

  if (!item) {
    res.json({ "status":"Product not found" });
    return;
  }

  // Get the current reserved stock for the item from Redis
  const currentQuantity = await getCurrentReservedStockById(itemId);
  const stock = 
    currentQuantity !== null ? currentQuantity : item.initialAvailableQuantity;
  item.currentQuantity = stock;
  res.json(item);
});

app.get('/reserve_product/:itemId', async (req, res) => {
  const itemId = Number(req.params.itemId);
  const item = getItemById(itemId);

  if (!item) {
    res.json({ "status":"Product not found" });
    return;
  }
  let currentQuantity = await getCurrentReservedStockById(itemId);
  if (currentQuantity === null) currentQuantity = item.initialAvailableQuantity;

  if (currentQuantity <= 0) {
    res.json({ status: "Not enough stock available", itemId: item.itemId });
    return;
  }
  reserveStockById(itemId, Number(currentQuantity) - 1);
  res.json({ status: "Reservation confirmed", itemId: item.itemId });
	
});

// Start the server
app.listen(port);
