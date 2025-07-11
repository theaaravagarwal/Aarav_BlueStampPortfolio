FROM ruby:3.1-alpine

RUN apk add --no-cache build-base ruby-dev libc6-compat git

WORKDIR /srv/jekyll

COPY Gemfile Gemfile.lock ./

RUN bundle install

COPY . .

CMD ["jekyll", "serve", "--host", "0.0.0.0"]
