package routers

import (
	"github.com/gin-gonic/gin"
	tranlation "github.com/gustavosantaella/src/modules/transalation/controllers"
)

func Run(engine *gin.Engine) {

	tranlation.Router(engine)

	engine.GET("/ping", func(ctx *gin.Context) {
		ctx.JSON(200, "pong")
	})
}
