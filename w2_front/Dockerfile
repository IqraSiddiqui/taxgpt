# Use Node.js as the base image for building the frontend assets
FROM node:14 as build

# Set the working directory in the container
WORKDIR /app

# Copy package.json and package-lock.json to the working directory
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy the rest of the application code
COPY . .

# Build the frontend assets
RUN npm run build

# Use Nginx as the base image for serving the frontend assets
FROM nginx:alpine

# Copy the built frontend assets from the previous stage to the Nginx web server directory
COPY --from=build /app/build /usr/share/nginx/html

# Expose port 80
EXPOSE 80

# Start the Nginx web server
CMD ["nginx", "-g", "daemon off;"]
