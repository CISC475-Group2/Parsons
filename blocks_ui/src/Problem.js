import React, { Component } from 'react';
import { DragSource, DragDropContext } from 'react-dnd';
import HTML5Backend from 'react-dnd-html5-backend';
import Block from './Block';
import BlockList from './BlockList';
import AvailableBlocksSpace from './AvailableBlocksSpace'

class Problem extends Component {
    getSubmitAlert() {
        switch (this.props.isSuccess) {
            case null:
                break;
            case true:
                return <div className="alert alert-success" role="alert">
                           <strong>Well done!</strong> That is the correct answer.
                       </div>
            case false:
                return <div className="alert alert-danger" role="alert">
                           <strong>Wrong answer.</strong> Change a few things up and try submitting again.
                       </div>
        }
    }
    render() {
        return (
            <div className="problem">
                <div className="page-header">
                      <h1>Problem {this.props.problemNumber}</h1>
                </div>
                <p>This should evaluate to <code>{this.props.evaluatesTo}</code></p>
                {this.getSubmitAlert.bind(this)()}
                <pre className="code-space">{this.props.baseBlockString}</pre>
                <pre>
                <Block block={this.props.baseBlock}
                       onMoveBlock={this.props.onMoveBlock}
                       onSwapBlocks={this.props.onSwapBlocks} />
                <AvailableBlocksSpace onMoveBlock={this.props.onMoveBlock}>
                    <BlockList blocks={this.props.blocks}
                               onMoveBlock={this.props.onMoveBlock}
                               onSwapBlocks={this.props.onSwapBlocks} />
                </AvailableBlocksSpace>
                </pre>
                <div className="btn-group" role="group" aria-label="...">
                    <button type="button" className="btn btn-default" onClick={this.props.onReset.bind(this)}>Reset</button>
                    <button type="button" className="btn btn-default" onClick={this.props.onSubmit.bind(this)}>Submit</button>
                </div>
            </div>
        );
    }
};

export default DragDropContext(HTML5Backend)(Problem);
