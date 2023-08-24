package remotes

import (
	"encoding/json"
	"fmt"
	"io"
	"net/http"
	"net/url"

	"github.com/gustavosantaella/src/helpers"
	"github.com/gustavosantaella/src/modules/transalation/structs"
)

func CallApiTranslate(from string, to string, text string) (*structs.ToTranslateStruct, error) {

	API_TRANSLATE := helpers.Env("API_TRANSLATION")

	values := url.Values{
		"origen":         {from},
		"texto_traducir": {text},
		"idioma_destino": {to},
	}
	response, err := http.PostForm(API_TRANSLATE, values)
	if err != nil {
		return nil, err
	}
	defer response.Body.Close()

	bodyIO, err := io.ReadAll(response.Body)

	fmt.Println(string(bodyIO))

	fmt.Println(from)
	fmt.Println(to)
	fmt.Println(text)
	data := structs.ToTranslateStruct{}
	json.Unmarshal([]byte(string(bodyIO)), &data)

	return &data, nil
}
