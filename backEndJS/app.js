const express = require("express");
const app = express();
const cors = require("cors");
const port = process.env.PORT || 3000; // Use the specified port or default to 3000

app.use(cors());

app.get("/api/version", (req, res) => {
  const version = process.env.APP_VERSION || "Version not specified"; // Retrieve version from environment variable
  res.json({ version }); // Respond with the version in JSON format
});

// Start the Express server
app.listen(port, () => {
  console.log(`Server is running on port ${port}`);
});
