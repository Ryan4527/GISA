from __future__ import annotations

from typing import List, Optional, Set, Tuple

import streamlit as st

Position = Tuple[int, int]


def is_knight_move(src: Position, dst: Position) -> bool:
    sr, sc = src
    dr, dc = dst
    return (abs(sr - dr), abs(sc - dc)) in {(1, 2), (2, 1)}


def init_game_state(board_size: int) -> None:
    st.session_state.board_size = board_size
    st.session_state.moves_made = 0
    st.session_state.knight_pos = None
    st.session_state.visited = set()
    st.session_state.history = [[0 for _ in range(board_size)] for _ in range(board_size)]
    st.session_state.message = "첫 칸을 눌러 기사의 시작 위치를 정하세요."


def place_knight(row: int, col: int) -> None:
    board_size: int = st.session_state.board_size
    knight_pos: Optional[Position] = st.session_state.knight_pos
    visited: Set[Position] = st.session_state.visited

    if knight_pos is not None:
        prev_r, prev_c = knight_pos
        st.session_state.history[prev_r][prev_c] = st.session_state.moves_made

    st.session_state.knight_pos = (row, col)
    visited.add((row, col))
    st.session_state.moves_made += 1

    remaining = board_size * board_size - st.session_state.moves_made
    st.session_state.message = (
        f"이동 수: {st.session_state.moves_made} | 남은 칸: {remaining} | 현재 위치: ({row + 1}, {col + 1})"
    )

    if st.session_state.moves_made == board_size * board_size:
        st.session_state.message = f"🎉 축하합니다! {board_size}x{board_size} 보드를 완주했습니다."


def on_cell_click(row: int, col: int) -> None:
    knight_pos: Optional[Position] = st.session_state.knight_pos
    visited: Set[Position] = st.session_state.visited

    if knight_pos is None:
        place_knight(row, col)
        return

    if (row, col) in visited:
        st.session_state.message = "이미 방문한 칸입니다. 다른 칸을 선택하세요."
        return

    if not is_knight_move(knight_pos, (row, col)):
        st.session_state.message = "유효하지 않은 이동입니다. 기사 규칙(L자)으로 이동하세요."
        return

    place_knight(row, col)


def board_cell_label(row: int, col: int) -> str:
    knight_pos: Optional[Position] = st.session_state.knight_pos
    value = st.session_state.history[row][col]

    if knight_pos == (row, col):
        return "♞"
    if value > 0:
        return str(value)
    return "·"


def render_board() -> None:
    board_size: int = st.session_state.board_size

    st.markdown("### 게임 보드")
    for r in range(board_size):
        cols = st.columns(board_size)
        for c in range(board_size):
            key = f"cell_{r}_{c}"
            label = board_cell_label(r, c)
            cols[c].button(label, key=key, use_container_width=True, on_click=on_cell_click, args=(r, c))


def main() -> None:
    st.set_page_config(page_title="Knight's Tour", layout="wide")
    st.title("Knight's Tour Game (Streamlit)")
    st.caption("보드 크기를 선택해서 기사(♞)가 모든 칸을 방문하도록 이동해보세요.")

    if "board_size" not in st.session_state:
        init_game_state(8)

    with st.sidebar:
        st.subheader("설정")
        selected_size = st.selectbox("보드 크기", options=[6, 7, 8, 9, 10], index=[6, 7, 8, 9, 10].index(st.session_state.board_size))

        if st.button("Start New Game", use_container_width=True):
            init_game_state(selected_size)

        if st.button("Restart", use_container_width=True):
            init_game_state(st.session_state.board_size)

        st.markdown("---")
        st.write(f"현재 보드: **{st.session_state.board_size} x {st.session_state.board_size}**")
        st.write(f"이동 수: **{st.session_state.moves_made}**")

    if selected_size != st.session_state.board_size:
        st.info("선택한 보드 크기를 적용하려면 **Start New Game**을 누르세요.")

    st.info(st.session_state.message)
    render_board()


if __name__ == "__main__":
    main()
