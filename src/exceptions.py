class FigureNotFoundError(Exception):
    def __init__(self, figure):
        self.message = f"Figure '{figure}' not found"
        super().__init__(self.message)
