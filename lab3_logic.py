import pandas as pd


def calculate_fare_by_sex(df: pd.DataFrame, func: str) -> pd.Series:
    """
    Вычисляет min/max/avg стоимость билетов для мужчин и женщин.
    :param df: DataFrame с колонками 'Sex' и 'Fare'
    :param func: 'min', 'max' или 'avg'
    :return: Series с результатами по полу
    """
    if func not in {"min", "max", "avg"}:
        raise ValueError(
            "Недопустимое значение func. Используйте 'min', 'max' или 'avg'.")

    if not {"Sex", "Fare"}.issubset(df.columns):
        raise ValueError("DataFrame должен содержать колонки 'Sex' и 'Fare'.")

    result = df.groupby("Sex")["Fare"].agg(
        min="min", max="max", avg="mean"
    )[func].round(2)

    return result
