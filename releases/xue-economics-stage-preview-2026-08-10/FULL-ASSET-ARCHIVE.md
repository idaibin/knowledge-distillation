# Full local asset archive

这份归档是 .codex/artifacts/ 的完整本地快照。v02 使用 COPYFILE_DISABLE=1 和 tar 的 --no-mac-metadata --no-xattrs --no-acls --no-fflags 生成，排除 AppleDouble、resource fork、xattr 和 ACL 污染；源资产未移动、未删除、未改写。

## Snapshot

| 项目 | 值 |
| --- | --- |
| Source root | .codex/artifacts/ |
| Source files | 790 regular files |
| Source bytes | 494,670,096 B / 471.754166 MiB |
| Source symlinks | 0 |
| Archive format | tar.gz |
| Archive member root | artifacts/ |
| Archive bytes | 489,246,024 B / 466.581367 MiB |
| Archive SHA-256 | 99955d014211cd63de30b9d74be10681369d7441b3112ab0bb23eee33950256f |
| Canonical archive filename | knowledge-distillation__assets__xue-economics-local__2026-08-10__v02.tar.gz |
| Drive upload parts | 6 parts, each at most 90 MiB (94,371,840 B) |

压缩率约为 98.9035%；源目录中 PNG、ZIP 等已压缩文件较多，因此不再生成第二种归档格式。

## Git 与 Drive 边界

- 约 467 MiB 的二进制归档不进入 Git；归档和分卷位于仓库外的 outputs/xue-economics-drive-upload/。
- Git release 跟踪说明、Drive 索引、源文件清单、分卷清单和校验文件；见 DRIVE-ASSET-INDEX.yaml。
- v01 归档和分卷保留在 outputs 并标记为 .superseded-appledouble；v01 不再是 Git/Drive 索引目标。工作树来源的旧 stage v02 也保留为 .superseded-worktree。
- 连接器单文件限制为 100 MiB；v02 全量资产使用 6 个不超过 90 MiB 的分卷。原始 v02 tar.gz 仍保留本地，不作为单文件上传。

## Drive logical paths

索引使用以下已确认的 logical paths，不写入 Google Drive 真实 ID 或 URL：

- AI Engineering Lab/40-Exports/Review-Packages/xue-economics/2026-08-10-stage-preview
- AI Engineering Lab/90-Archive/xue-economics/2026-08-10-full-assets

v02 本地归档和索引已完成尺寸、SHA-256、成员集合审计；Drive 中原 v01 文件已原位替换为 v02，未创建重复项，11 个文件均已通过名称、字节数、父目录和目录计数 readback，索引状态为 verified。

## Verify source snapshot

在仓库根目录执行：

    awk -F '\t' '{n += 1; bytes += $2} END {printf "files=%d bytes=%d MiB=%.6f\n", n, bytes, bytes/1048576}' \
      releases/xue-economics-stage-preview-2026-08-10/FULL-ASSET-SHA256.tsv

预期：files=790 bytes=494670096 MiB=471.754166。

## Verify v02 archives with Python tarfile

下面的验收命令同时检查 full 与 stage：regular member 集合、字节总和、AppleDouble (._*)、绝对路径、.. 路径，以及 stage 每个 member 的字节是否等于 git show HEAD:path。它是主要验收，不以 tar | wc 作为集合证明。

    python3 - /path/to/xue-economics-drive-upload <<'PY'
    import hashlib
    from pathlib import Path
    import subprocess
    import sys
    import tarfile

    repo = Path.cwd()
    out = Path(sys.argv[1]).resolve()

    def safe_members(tf):
        members = tf.getmembers()
        bad = [
            m.name
            for m in members
            if m.name.startswith("/")
            or ".." in Path(m.name).parts
            or any(part.startswith("._") for part in Path(m.name).parts)
            or m.issym()
            or m.islnk()
        ]
        assert not bad, bad[:10]
        return members

    source_root = repo / ".codex/artifacts"
    source_files = {
        f"artifacts/{p.relative_to(source_root).as_posix()}"
        for p in source_root.rglob("*")
        if p.is_file()
    }
    source_bytes = sum(
        (source_root / name.removeprefix("artifacts/")).stat().st_size
        for name in source_files
    )
    expected_full = {}
    for line in (repo / "releases/xue-economics-stage-preview-2026-08-10/FULL-ASSET-SHA256.tsv").read_text().splitlines():
        sha256, size, path = line.split("\t", 2)
        expected_full[path.removeprefix(".codex/")] = (sha256, int(size))

    full = out / "knowledge-distillation__assets__xue-economics-local__2026-08-10__v02.tar.gz"
    with tarfile.open(full, "r:gz") as tf:
        members = safe_members(tf)
        regular = {m.name for m in members if m.isfile()}
        assert regular == source_files
        assert sum(m.size for m in members if m.isfile()) == source_bytes == 494670096
        assert regular == set(expected_full)
        for member in members:
            if member.isfile():
                payload = tf.extractfile(member).read()
                expected_sha, expected_size = expected_full[member.name]
                assert len(payload) == expected_size == member.size, member.name
                assert hashlib.sha256(payload).hexdigest() == expected_sha, member.name
    print(f"full PASS regular={len(source_files)} bytes={source_bytes}")

    stage_git = "releases/xue-economics-stage-preview-2026-08-10"
    stage_root = "xue-economics-stage-preview-2026-08-10/"
    tracked = subprocess.check_output(
        ["git", "ls-tree", "-r", "--name-only", "HEAD", stage_git],
        cwd=repo,
        text=True,
    ).splitlines()
    stage_files = {
        stage_root + p.removeprefix(stage_git + "/")
        for p in tracked
    }
    stage = out / "knowledge-distillation__release__xue-economics-stage-preview__2026-08-10__v02.tar.gz"
    with tarfile.open(stage, "r:gz") as tf:
        members = safe_members(tf)
        regular = {m.name for m in members if m.isfile()}
        assert regular == stage_files
        for member in members:
            if member.isfile():
                git_path = stage_git + "/" + member.name.removeprefix(stage_root)
                expected = subprocess.check_output(
                    ["git", "show", f"HEAD:{git_path}"],
                    cwd=repo,
                )
                assert tf.extractfile(member).read() == expected, git_path
    print(f"stage PASS regular={len(stage_files)} HEAD byte matches={len(stage_files)}")
    PY

预期：full PASS regular=790 bytes=494670096；stage PASS regular=91 HEAD byte matches=91。

## Reassemble Drive parts

在下载完 part-01-of-06 至 part-06-of-06 后，先在同一目录校验分卷，再按自然序拼接：

    shasum -a 256 -c FULL-ASSET-PARTS-SHA256SUMS
    cat \
      knowledge-distillation__assets__xue-economics-local__2026-08-10__v02.part-01-of-06 \
      knowledge-distillation__assets__xue-economics-local__2026-08-10__v02.part-02-of-06 \
      knowledge-distillation__assets__xue-economics-local__2026-08-10__v02.part-03-of-06 \
      knowledge-distillation__assets__xue-economics-local__2026-08-10__v02.part-04-of-06 \
      knowledge-distillation__assets__xue-economics-local__2026-08-10__v02.part-05-of-06 \
      knowledge-distillation__assets__xue-economics-local__2026-08-10__v02.part-06-of-06 \
      > knowledge-distillation__assets__xue-economics-local__2026-08-10__v02.tar.gz
    shasum -a 256 -c ARCHIVE-SHA256SUMS

分卷按固定字节边界从同一 v02 tar.gz 生成；不得重新压缩、排序或改名后再拼接。

## Stage release upload

阶段 release 归档只包含 Git HEAD 中的 91 个 release 文件，不包含本说明和其他新增清单：

- 文件名：knowledge-distillation__release__xue-economics-stage-preview__2026-08-10__v02.tar.gz
- 大小：53,375,543 B / 50.902884 MiB
- SHA-256：88132896471a88af5dfbee4cb456443433772a8afb8528fe168e377b0a695739

该文件满足 100 MiB 单文件限制；Drive v01 文件已原位替换为 v02，并以 STAGE-RELEASE-SHA256SUMS 完成校验。
