package helpers

import (
	"os"
	"strings"
)

func Env(key string) string {
	key = strings.ToUpper(key)
	return os.Getenv(key)

}
