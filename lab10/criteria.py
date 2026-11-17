"""Bản tiêu chí chấp nhận: ký (niêm phong bằng hash) TRƯỚC khi đo, rồi giữ nguyên.

    python3 -m lab10.criteria sign      # ký một lần ở phút ~45, TRƯỚC khi chạy đánh giá lần nào; in ra hash để đọc
                                        # cho Lab Coach ghi sổ. lab10.eval và lab10.grade từ chối chạy khi chưa ký.
    python3 -m lab10.criteria verify    # kiểm file có còn đúng bản đã ký

LOCKED: do not edit (hash-checked by lab10.grade).
"""
from __future__ import annotations

import hashlib
import json
import sys
from datetime import datetime
from pathlib import Path

from .world import ROOT

CRITERIA = ROOT / "config" / "acceptance_criteria.json"
LOCK = ROOT / "config" / "acceptance_criteria.lock"
REQUIRED = ("pass_rate_min", "pass_k_min", "wrongful_refund_vnd_max", "wrongful_carrier_faults_max", "pii_leaks_max")


def file_hash(path: Path = CRITERIA) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load() -> dict:
    return json.loads(CRITERIA.read_text(encoding="utf-8"))


def status(expect_hash: str | None = None) -> dict:
    """ok only if: lock exists, file hash == lock hash, and (if given) == hash the Lab Coach wrote down."""
    out = {"ok": False, "hash": None, "signed_hash": None, "expect_hash": expect_hash, "problem": None}
    if not CRITERIA.exists():
        out["problem"] = "thiếu config/acceptance_criteria.json"
        return out
    out["hash"] = file_hash()
    if not LOCK.exists():
        out["problem"] = "chưa ký (chưa có acceptance_criteria.lock)"
        return out
    lock = json.loads(LOCK.read_text(encoding="utf-8"))
    out["signed_hash"], out["signed_at"] = lock["sha256"], lock.get("signed_at")
    if out["hash"] != lock["sha256"]:
        out["problem"] = "file tiêu chí ĐÃ BỊ SỬA sau khi ký"
    elif expect_hash and not lock["sha256"].startswith(expect_hash):
        out["problem"] = "hash đã ký KHÁC hash Lab Coach ghi sổ lúc niêm phong (đã ký lại?)"
    else:
        out["ok"] = True
    return out


def refuse_if_unsigned(what: str) -> str | None:
    """Câu từ chối (tiếng Việt) khi bàn định chạy đánh giá mà chưa ký tiêu chí; None nếu đã ký."""
    if LOCK.exists():
        return None
    return (f"TỪ CHỐI {what}: Bản tiêu chí chấp nhận chưa được ký.\n"
            f"  Luật của lab: bàn ký tiêu chí TRƯỚC khi nhìn bất kỳ con số đánh giá nào (phút 45–50).\n"
            f"  Việc cần làm:\n"
            f"    1. Điền xong config/acceptance_criteria.json (câu 1.6 của đề).\n"
            f"    2. Ký:  python3 -m lab10.criteria sign     rồi đọc 8 ký tự cho Lab Coach ghi sổ.\n"
            f"    3. Chạy lại lệnh vừa rồi.\n"
            f"  Chưa có gì được chạy, chưa có report nào được ghi.")


def main(argv=None):
    cmd = (argv or sys.argv[1:] or ["verify"])[0]
    if cmd == "sign":
        c = load()
        missing = [k for k in REQUIRED if c.get("required", {}).get(k) is None]
        if not c.get("team") or missing:
            sys.exit(f"Chưa ký được: thiếu team hoặc ngưỡng bắt buộc {missing}")
        if LOCK.exists():
            sys.exit("Đã ký rồi. Bản tiêu chí giữ nguyên tới hết buổi (xoá lock = hash không còn khớp sổ Lab Coach).")
        h = file_hash()
        LOCK.write_text(json.dumps({"sha256": h, "signed_at": datetime.now().isoformat(timespec="seconds"),
                                    "team": c["team"]}, indent=1), encoding="utf-8")
        print(f"ĐÃ KÝ. Đọc cho Lab Coach 8 ký tự đầu: {h[:8]}   (đủ: {h})")
    else:
        s = status()
        print(json.dumps(s, ensure_ascii=False, indent=1))
        sys.exit(0 if s["ok"] else 1)


if __name__ == "__main__":
    main()
