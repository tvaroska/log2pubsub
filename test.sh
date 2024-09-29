curl -X POST -H 'Authorization: Bearer sk-1234' -H "Content-type: application/json" -d '{ \
  "model": "flash", \
  "prompt": "1",
  "question": "What is the capital of Slovakia?"
}' 'http://0.0.0.0:4000/v1/chat/completions'









  "messages": [ \
    { \
      "role": "system", \
      "content": "You are a helpful assistant." \
    }, \
    { \
      "role": "user", \
      "content": "Who won the world series in 2020?" \
    }, \
    { \
      "role": "assistant", \
      "content": "The Los Angeles Dodgers won the World Series in 2020." \
    }, \
    { \
      "role": "user", \
      "content": "Where was it played?" \
    } \
  ] \
}' 'http://0.0.0.0:4000/v1/chat/completions'
