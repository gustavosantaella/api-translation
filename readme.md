
# API translation service

You can use this API to transalate text.
## Demo

You can test the api here [Test api here](https://ms-countries.onrender.com/)
## API Reference

#### Get translation

```http
  GET /translate/to?from={from}&to={to}&text={text}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `to`      | `string` | **Required**. Language to translate |
| `from`      | `string` | **Required**. Language from translate |
| `text`      | `string` | **Required**. Text to translate |

## Tech Documentation

- [Gin framework](https://github.com/gin-gonic/gin)
- [Go](https://github.com/go-pg/pg)

## Contact

softlink.ve@gmail.com
