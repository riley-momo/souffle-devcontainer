FROM ubuntu:24.04

ENV DEBIAN_FRONTEND=noninteractive

# Install all required dependencies
RUN apt-get update \
        && apt-get install -y \
  bison \
  build-essential \
  clang \
  cmake \
  doxygen \
  flex \
  g++ \
  git \
  libffi-dev \
  libncurses5-dev \
  libsqlite3-dev \
  make \
  mcpp \
    python3 \
  python3-pip \
  sqlite3 \
  zlib1g-dev \
    && rm -rf /var/lib/apt/lists/*

# Clone, configure, build, and install Souffle
RUN git clone --depth 1 https://github.com/souffle-lang/souffle.git /tmp/souffle \
    && cd /tmp/souffle \
    && cmake -S . -B build -DCMAKE_INSTALL_PREFIX=/usr/local \
    && cmake --build build -j $(nproc) \
    && cmake --build build --target install \
    && rm -rf /tmp/souffle

WORKDIR /tmp/python-wrapper
COPY pyproject.toml ./
COPY souffle ./souffle
RUN python3 -m pip install --break-system-packages . \
  && rm -rf /tmp/python-wrapper

# Create a non-root user for development
ARG USERNAME=dev
ARG USER_UID=1000
ARG USER_GID=$USER_UID
RUN if ! getent group "$USER_GID" >/dev/null; then groupadd --gid "$USER_GID" "$USERNAME"; fi \
  && if ! id -u "$USERNAME" >/dev/null 2>&1; then \
    if getent passwd "$USER_UID" >/dev/null; then \
      useradd --gid "$USER_GID" -m "$USERNAME"; \
    else \
      useradd --uid "$USER_UID" --gid "$USER_GID" -m "$USERNAME"; \
    fi; \
  fi

USER $USERNAME
