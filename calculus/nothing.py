from time import sleep
from typing import Type, NamedTuple, Iterable, Generator, Self

from act import fun, indexed, flat, partial
from act.cursors.static import s


type Nothing = Void | Disturbance | Space | SpaceTime
type Void = None | Disturbance

Space: Type[list[Void]] = list


class Disturbance(NamedTuple):
    a: Void
    b: Void


class SpaceTime:
    boundaries_of_past_expansions = property(fun(s.__boundaries_of_past_expansions))

    def __init__(
        self,
        *voids: Void,
        boundaries_of_past_expansions: Iterable[int] = tuple(),
    ) -> None:
        self.__voids = list(voids)
        self.__boundaries_of_past_expansions = list(boundaries_of_past_expansions)

        self.__normalize()

    def __iter__(self) -> Generator[Space, None, None]:
        boundaries = indexed(self.__boundaries_of_past_expansions, 0, 1)

        for left_boundary, right_boundary in boundaries:
            yield self.__voids[left_boundary:right_boundary]

    def expand(self) -> None:
        self.__boundaries_of_past_expansions.append(len(self.__voids))

        past = self.__voids[:self.__boundaries_of_past_expansions[-2]]
        present = self.__voids[self.__boundaries_of_past_expansions[-2]:]

        for past_void in past:
            for present_void in present:
                self.__voids.append(Disturbance(past_void, present_void))
                self.__voids.append(Disturbance(present_void, past_void))

        for first_void in present:
            for second_void in present:
                self.__voids.append(Disturbance(first_void, second_void))

    @classmethod
    def of(cls, *spaces: Iterable[Void]) -> Self:
        return cls(
            *flat(spaces),
            boundaries_of_past_expansions=map(len, spaces[:-1]),
        )

    def __normalize(self) -> None:
        if len(self.__boundaries_of_past_expansions) != 0:
            assert max(self.__boundaries_of_past_expansions) <= len(self.__voids)

        assert (
            self.__boundaries_of_past_expansions
            == sorted(self.__boundaries_of_past_expansions)
        )

        assert all(
            boundary >= 0 for boundary in self.__boundaries_of_past_expansions
        )

        if (
            len(self.__boundaries_of_past_expansions) == 0
            or self.__boundaries_of_past_expansions[-1] != 0
        ):
            self.__boundaries_of_past_expansions.insert(0, 0)


def undefine() -> SpaceTime:
    return SpaceTime(None)


def repr_of(nothing: Nothing, *, _is_nested: bool = False) -> str:
    if nothing is None:
        return 'v'

    if isinstance(nothing, Disturbance):
        nested_repr_of = partial(repr_of, _is_nested=True)
        repr_ = f"{nested_repr_of(nothing.a)} -> {nested_repr_of(nothing.b)}"

        return f"({repr_})" if _is_nested else repr_

    if isinstance(nothing, Space):
        return f"Space({"; ".join(map(repr_of, nothing))})"

    if isinstance(nothing, SpaceTime):
        return f"SpaceTime({" --> ".join(map(repr_of, nothing))})"


def show(spacetime: SpaceTime) -> None:
    subject = spacetime if len(tuple(spacetime)) == 0 else tuple(spacetime)[-1]
    print(repr_of(subject), "\n")

    sleep(2)


def main() -> None:
    spacetime = undefine()

    while True:
        show(spacetime)
        spacetime.expand()


if __name__ == "__main__":
    main()

