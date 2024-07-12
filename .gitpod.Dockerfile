FROM gitpod/workspace-full:latest

# Install wget
RUN sudo apt-get update && sudo apt-get install -y wget

# Install any additional dependencies if needed
