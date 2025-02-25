# Use the official lightweight Nginx image
FROM nginx:alpine

# Copy custom Nginx configuration into the container
COPY nginx.conf /etc/nginx/conf.d/default.conf

# Expose port 80 for HTTP traffic
EXPOSE 80

# Start Nginx
CMD ["nginx", "-g", "daemon off;"]
