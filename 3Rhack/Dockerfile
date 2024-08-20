# Stage 1: Build the Svelte app
FROM node:20-alpine AS build

# Set the working directory in the container
WORKDIR /app

# Copy package.json and package-lock.json to the container
COPY package*.json ./

# Install dependencies
RUN npm ci

# Copy the rest of the application to the container
COPY . .

# Build the Svelte app
RUN npm run build

# Expose the port
EXPOSE 5173

# Run the server script
CMD npm run dev
