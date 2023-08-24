package tranlation

import (
	"fmt"

	"github.com/gin-gonic/gin"
	"github.com/gustavosantaella/src/modules/transalation/services"
)

func Router(engine *gin.Engine) {

	engine.GET("/translate/to", func(ctx *gin.Context) {
		to := ctx.Query("to")
		from := ctx.Query("from")
		toTranslate := ctx.Query("text")
		response, err := services.Translate(from, to, toTranslate)
		if err != nil {
			fmt.Println(err)
			ctx.JSON(400, "An error ocurred")
			return
		}
		ctx.JSON(200, response)
	})
}
