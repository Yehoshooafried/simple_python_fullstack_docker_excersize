# Use an official Node.js runtime as a parent image
FROM node:14

# Set the working directory in the container
WORKDIR /app

# Copy package.json and package-lock.json to the working directory
COPY package*.json ./

# Install app dependencies
RUN npm install

# Copy the rest of the application source code to the working directory
COPY . .

# Expose the port your app will run on (replace 3000 with your actual port)
EXPOSE 3000

# Define the command to start your Node.js application
CMD [ "node", "app.js" ]
