package main

import (
	"github.com/gin-gonic/gin"
	"github.com/gustavosantaella/src/routers"
	"github.com/joho/godotenv"
)

func main() {
	godotenv.Load()

	r := gin.Default()

	routers.Run(r)

	r.Run("0.0.0.0:8000")

}
