FROM rust:alpine

RUN apk add --no-cache musl-dev python3 py3-pip
RUN cargo install cfn-guard
RUN pip install cfn_guard_test

WORKDIR /tests
