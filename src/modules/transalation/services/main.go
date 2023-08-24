package services

import (
	"github.com/gustavosantaella/src/modules/transalation/remotes"
	"github.com/gustavosantaella/src/modules/transalation/structs"
)

func Translate(from string, to string, toTranslate string) (*structs.ToTranslateStruct, error) {
	data, err := remotes.CallApiTranslate(from, to, toTranslate)

	if err != nil {
		return nil, err
	}

	return data, nil
}
