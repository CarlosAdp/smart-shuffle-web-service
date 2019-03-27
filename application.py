from utils.decorators import force_type
import flask

@force_type
class Application():
    app = flask.app.Flask
    name = "shuffle"

    @classmethod
    def init(cls : type) -> None:
        cls.app = flask.app.Flask(cls.name)

        @cls.app.route("/generate", methods = ["GET"])
        def generate_shuffled_playlist() -> str:
            token = flask.request.args.get("token")
            first_song_id = flask.request.args.get("first_song_id")
            return "SHUFFLE_{}_{}".format(token, first_song_id)

        # Methods definition
        @cls.app.route("/update", methods = ["GET"])
        def update_local_library() -> str:
            token = flask.request.args.get("token")
            return "UPDATE_{}".format(token)

    @classmethod
    def run(cls : type) -> None:
        cls.app.run()
