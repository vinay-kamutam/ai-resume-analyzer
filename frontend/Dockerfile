# Base Image
FROM node:22-alpine

# Working Directory
WORKDIR /app

# Copy package files
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy project
COPY . .

# Expose Vite Port
EXPOSE 5173

# Start React
CMD ["npm", "run", "dev", "--", "--host"]